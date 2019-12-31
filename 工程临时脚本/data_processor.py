# -*- coding: utf-8 -*-
import asyncio
import json
import traceback
from asyncio.base_futures import CancelledError

from bson import ObjectId
from loguru import logger

import g_vars
from biz.biz_candidate import BizCandidate
from biz.biz_contents import BizContents
from biz.biz_dailypops import BizDailypops
from biz.biz_webpage import BizApps, BizDalaoshuo, BizWebDetail, BizWeixin
from common.httpclient import AsyncRequests
from common.util import is_not_empty, get_time_str
from config import config
from config.config_json import ConfigJson


class DataProcessor(object):
    def __init__():
        # 建立一个 BizCandidate 对象，用于操作候选集数据表 recommend_candidate
        biz_candidate = BizCandidate()

    async def process_by_biz_type(, biz_type_list=None, language_type=""):
        """
        将所有数据源的数据处理后存入候选集表
        :param biz_type_list:
        :param language_type: 语言标识，如英文用 en
        :return:
        """
        if not biz_type_list:
            if not language_type:
                config_file_path = "./config/config_biz_type.json"
            else:
                config_file_path = "./config/config_biz_type_" + language_type + ".json"
            # 从配置文件获取所有数据源类型
            biz_type_list = get_all_biz_type(config_file_path)
            if not biz_type_list:
                return
        # 遍历列表，对每个业务类型进行处理
        # 创建任务列表，调用 asyncio.gather 并行处理
        task_list = []
        for biz_type in biz_type_list:
            task_list.append(process_source_data_loop(biz_type))
        await asyncio.gather(*task_list)

    async def process_source_data_loop(, biz_type):
        """
        根据条件循环执行数据处理
        :param biz_type:
        :return:
        """
        try:
            logger.info(biz_type + " : ETL 开始，数据处理中 ")
            # 运行一次获取一个边界条件
            id_boundary = await process_source_data(biz_type)
            # 存在边界条件时继续执行
            while id_boundary:
                logger.info('process_source_data_loop', biz_type)
                # 每次处理 n 条，防止内存超载
                # 返回 True 表示可能还有数据未处理
                # 连续执行直到返回 False，表示目前已无符合条件的源数据
                id_boundary = await process_source_data(biz_type, id_boundary)
            logger.info(biz_type + " : ETL 结束，本轮数据处理完毕 ")
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error(str(e))

    async def process_source_data(, biz_type, id_boundary=None):
        """
        TODO 从单进程改为并发处理
        根据业务类型查询源数据，处理后进入候选集表
        :param id_boundary:
        :param biz_type:
        :return:
        """
        try:
            # 获取数据库连接对象
            biz_obj = get_biz_obj(biz_type)
            # 获取 table 对象
            table = biz_obj.get_table()

            # 定义一个词典存储源数据表的查询条件
            query_param = {}

            # 不存在传入边界则查询获取边界
            if not id_boundary:
                # 获取候选集中的查询边界，此处为最新一条记录的 id
                id_boundary = await biz_candidate.get_lower_boundary_by_biz(biz_type)

            if id_boundary and id_boundary != "None":
                # 只查询晚于给定主键的数据
                query_param = {"_id": {'$gt': ObjectId(id_boundary)}}
                # 存在 id 下边界，所以按照正序排列
                sort = g_vars.CandidateFilters.ASCENDING.value
            else:
                # 没有边界，则默认按照倒序获取数据
                sort = g_vars.CandidateFilters.DESCENDING.value

            # 获取源数据字段
            source_fields, hidden_fields, timestamp_length, query_condition = get_source_fields(biz_type)

            # 添加附带的查询条件
            if query_condition:
                query_param.update(query_condition)

            # 根据条件查询结果总数
            count = await table.count_documents(query_param)
            # 如果总数等于 0，终止处理数据
            if count == 0:
                # 返回空
                return None
            # IO 操作，从 mongodb 查询数据
            cursor = table.find(query_param)
            # 源表按照指定的索引和顺序排列
            cursor.sort([("_id", sort)])

            # 限制单次查询上限，避免内存过载
            cursor.limit(g_vars.CandidateFilters.process_limit_per_once.value)

            success_count = 0  # 统计成功条数
            excluded_count = 0  # 统计排除的条数
            result_list = []
            # 遍历获取数据
            async for item in cursor:
                # 存储主键，用于下一轮调用此方法时作为下边界
                id_boundary = item['_id']
                # 处理单条数据，排除不符合条件的数据
                # 添加到任务列表，用于下一步并发
                result = await process_one_item(source_fields, hidden_fields, item, biz_type, biz_obj)
                result_list.append(result)

            # 统计入库结果
            for result in result_list:
                if result:
                    success_count += 1
                else:
                    excluded_count += 1
            # 处理完成后打印一次全量统计信息
            count_and_print(success_count, excluded_count)
        except CancelledError as e:
            logger.error(traceback.format_exc())
            logger.error(str(e))
            return str(id_boundary)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error(str(e))
            return None
        return str(id_boundary)

    async def process_one_item(, source_fields, hidden_fields, item, biz_type, biz_obj):
        try:
            # 通过配置文件的字段映射，将源数据对象转化为候选集数据对象
            record = exchange_field_name(source_fields, hidden_fields, item)
            # 当前类型的一些特殊处理
            record = biz_obj.special_treat(item, record)
            # 特殊处理后如果返回 None，说明特殊处理筛除了当前项
            if not record:
                return 0
            # 根据过滤条件筛掉不符合条件的一部分数据
            if not content_filter(record, biz_type):
                return 0  # 返回 0，不存储到数据库
            # 检查摘要
            record = await treat_abstract(record)
            # 检查 nlp 结果
            record = await treat_nlp(record)

            record['biz_type'] = biz_type  # 保存业务类型
            record['create_time'] = get_time_str()  # 本条数据创建时间
            # 向候选集插入当前数据
            return await biz_candidate.insert_one(record)
        except Exception as e:
            # 获取日志信息
            logger_msg = construct_logger_msg(str(item["_id"]), str(e), biz_type)
            # 打印日志信息
            logger.error(logger_msg)
            return 0  # 返回 0，不存储到数据库

    def content_filter(, record, biz_type=""):
        """
        内容过滤条件
        :param biz_type:
        :param record:
        :return:
        """
        # 打印在日志里的提示信息
        message = None
        # 源数据表主键非空
        # 当前程序根据 mongodb 的主键为数据排序
        # 如果源表 id 为空，无法对照源表和目标表的数据先后
        if not is_not_empty(record.get('origin_id')):
            message = "源表主键为空"
        # 标题非空
        if not is_not_empty(record.get('title')):
            message = "标题为空"
        # 内容非空
        if not is_not_empty(record.get('content')):
            message = "内容为空"
        # url 非空
        if not is_not_empty(record.get('path')):
            message = "url 为空"
        # 内容字数不能小于最少字数限制
        if len(record.get('content')) < g_vars.CandidateFilters.content_minimum_count.value:
            message = "内容字数过少"
        if message:
            # 获取日志信息
            logger_msg = construct_logger_msg(record['origin_id'], message + " 不符合过滤条件", biz_type)
            # 打印日志信息
            logger.info(logger_msg)
            # 不符合过滤条件返回 False
            return False
        # 符合条件返回 True
        return True

    @staticmethod
    def exchange_field_name(field_map, hidden_fields, source_item, target_item=None):
        """
        来自数据源的单条数据 source_item 字段名各不相同
        通过事先定义的配置文件中的字段名映射 field_map
        将源数据对应到推荐候选集表中的字段
        :param hidden_fields:
        :param target_item: 目标对象，存入推荐候选集表
        :param field_map: 字段名映射关系
        :param source_item: 来自数据源的单条记录
        :return:
        """
        # 初始化目标对象
        if target_item is None:
            target_item = {}
        # 遍历字段映射，将源对象映射到目标对象
        for key in field_map:
            # field_map 中的 key 是推荐候选集中的字段名
            # field_map 中某个 key 对应的 value 就是源数据中的字段名
            # 通过 field_map[key] 从映射关系中获得源数据中的字段名称
            source_key = field_map[key]
            # 通过 source_key 从数据中获取对应的值
            target_value = source_item.get(source_key)
            # 将 source_value 赋值给推荐候选集对象相应的字段
            target_item[key] = target_value

        # 获取源数据 ID
        origin_id = source_item.get('_id')
        # 如果是 ObjectId 则转为 str
        if isinstance(origin_id, ObjectId):
            origin_id = str(origin_id)
        target_item['origin_id'] = origin_id

        # 将隐藏字段信息添加到数据中
        if hidden_fields:
            target_item.update(hidden_fields)
        return target_item

    @staticmethod
    def get_source_fields(biz_type):
        """
        获取源数据表相关字段
        :param biz_type:
        :return:
        """
        # 通过配置文件获取所有数据源信息
        biz_source_all = ConfigJson.from_json_file("./config/config_biz_source.json")
        try:
            # 通过业务类型获取当前数据源信息
            biz_source = biz_source_all[biz_type]
            # 获取当前数据源的数据库名称
            source_db = biz_source['database']
            # 获取当前数据源的数据表名称
            source_table = biz_source['table']
        except KeyError as e:
            raise KeyError(e)

        # 从配置文件获取所有源数据的字段名对应关系
        all_field_pairs = ConfigJson.from_json_file("./config/config_field.json")
        # 通过数据库和表名，获取当前源数据的字段名对应关系
        source_fields = all_field_pairs[source_db][source_table]

        # 获取隐藏字段，如爬虫数据，没有字段表示内容类型，但是内容类型默认都是 html
        hidden_fields = biz_source.get('hidden_fields')
        if not hidden_fields:
            hidden_fields = {}

        # 获取时间戳的位数
        timestamp_length = biz_source.get("timestamp_length")
        if not timestamp_length:
            timestamp_length = 13  # 默认时间戳为 13 位

        # 获取其他查询条件
        query_condition = biz_source.get("query_condition")
        if not query_condition:
            query_condition = {}

        return source_fields, hidden_fields, timestamp_length, query_condition

    @staticmethod
    async def sensitive_check(content):
        """
        敏感词检测
        :param content:
        :return:
        """
        msg = await AsyncRequests.post(url=config.SENSITIVE.CHECK_SENSITIVE_URL, payload={'text': content})
        if msg:
            msg = json.loads(msg)
            has = msg.get('data').get('has')
            return has
        else:
            raise Exception("敏感词接口调用出错 ")

    @staticmethod
    async def nlp_transform(content):
        """
        调用 nlp 接口
        :param content:
        :return:
        """
        res = await AsyncRequests.post(url=config.YL_SERVER.NLP_SERVR_V2, payload={'content': content})
        if res:
            return json.loads(res)
        else:
            raise Exception("NLP 接口调用出错")

    @staticmethod
    def extract_nlp_result(nlp_result):
        """
        将接口生成的 nlp 的结果提取为固定的格式
        :param nlp_result:
        :return:
        """
        nlp_item = {}
        try:
            if not nlp_result:
                return nlp_item
            # 获取分类
            # 分类的数据结构是包含了一组字典的列表 [{topic:xx, score: xx}]
            # 其中的 score 是百分比
            old_category_list = nlp_result.get("type")
            if old_category_list:
                category_dict_list = []
                # 将 topic 字段替换为 tag，与 entity 和 label 统一，便于处理
                for category in old_category_list:
                    category_dict = {"tag": category["topic"],
                                     "score": category["score"]}
                    category_dict_list.append(category_dict)
                nlp_item["category"] = category_dict_list

            # nlp_result["weight"] 是 dict 结构
            # 包含了标签和实体中所有个体的权重
            weight_dict = nlp_result.get("weight")
            if weight_dict:
                # 获取标签，标签的内容是包含了一组字符串的列表 [xx, xx]
                old_label_list = nlp_result["label"]["content"]
                if old_label_list:
                    # 分布遍历 label_list 和 entity_list，从 weight_dict 中找出对应的权重
                    label_dict_list = []
                    for label in old_label_list:
                        # 用 label 的值为键，找到对应的 score
                        score = weight_dict[label]
                        label_dict = {'tag': label, "score": score}
                        label_dict_list.append(label_dict)
                    nlp_item["label"] = label_dict_list

                # 获取实体，实体的内容是包含了一组 dict 的列表 [{entity:xx, property: xx}]
                old_entity_list = nlp_result.get("entity2property")
                if old_entity_list:
                    entity_dict_list = []
                    for entity in old_entity_list:
                        entity_dict = {"tag": entity["entity"],
                                       "name": entity["property"]}
                        entity_dict_list.append(entity_dict)
                    nlp_item["entity"] = entity_dict_list
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error(str(e))
        return nlp_item

    async def generate_abstract(, content):
        """
        调用接口 生成摘要
        :param content:
        :return:
        """
        res = await AsyncRequests.post(url=config.YL_SERVER.AUTO_ABSTRACT_SERVER, payload={'content': content})
        if res:
            return check_abstract(res)
        raise Exception("摘要为空或接口调用出错")

    @staticmethod
    def check_abstract(abstract):
        """
        检查摘要是否符合要求
        :param abstract:
        :return:
        """
        if abstract and abstract.strip():
            # 摘要不能少于最少字数
            if len(abstract) >= g_vars.CandidateFilters.abstract_minimum_count.value:
                return abstract
            else:
                raise Exception("摘要字数不足")
        else:
            raise Exception("摘要为空")

    @staticmethod
    def count_and_print(success_count, excluded_count):
        """
        计数并打印消息
        :param success_count: 成功条数
        :param excluded_count: 排除条数
        :return:
        """
        logger.info(str(success_count + excluded_count) + " records processed")
        logger.info(str(success_count) + " records success")
        logger.info(str(excluded_count) + " records excluded")

    @staticmethod
    def construct_logger_msg(biz_id, message, biz_type=""):
        """
        打印一条日志
        :param biz_type: 业务类型
        :param biz_id: 业务 id
        :param message: 打印信息
        :return:
        """
        logger_msg = "\n=== "
        if biz_type:
            logger_msg += "业务类型 : " + biz_type + "; "
        logger_msg += " 源数据 ID : " + biz_id + " ===\n"
        logger_msg += "筛除原因：" + message
        return logger_msg

    @staticmethod
    def get_biz_obj(biz_type):
        """
        根据业务类型获取相关的数据库连接
        TODO 处理数据源改为通用接口，可以对特殊情况用脚本处理
        :param biz_type:
        :return:
        """
        if biz_type == "crawl_apps":
            return BizApps()
        elif biz_type == "crawl_dalaoshuo":
            return BizDalaoshuo()
        elif biz_type == "crawl_webdetail":
            return BizWebDetail()
        elif biz_type == "crawl_weixin":
            return BizWeixin()
        elif biz_type == "dailypops":
            return BizDailypops()
        elif "soucang" in biz_type:
            return BizContents()

    @staticmethod
    def get_all_biz_type(config_file_path):
        """
        获取所有源数据类型
        :return:
        """
        if not config_file_path:
            return None
        biz_type_dict = ConfigJson.from_json_file(config_file_path)
        biz_type_list = []
        for parent in biz_type_dict:
            one_parent = biz_type_dict[parent]
            # 如果存在子列表，从子列表读取
            sub_list = one_parent.get('sub')
            if sub_list:
                for sub_key in sub_list:
                    one_sub = sub_list.get(sub_key)
                    if one_sub:
                        biz_type = one_sub.get('biz_type')
                        if biz_type:
                            biz_type_list.append(biz_type)
            else:
                # 否则直接读取父类型
                biz_type = parent.get('biz_type')
                if biz_type:
                    biz_type_list.append(biz_type)
        return biz_type_list

    async def treat_abstract(, record):
        """
        处理摘要
        :param record:
        :return:
        """
        abstract = record.get('abstract')  # 摘要

        content = record.get('content')  # 完整内容

        if not abstract:
            abstract = await generate_abstract(content)
        # 检查摘要
        abstract = check_abstract(abstract)

        # 存入摘要
        record['abstract'] = abstract
        return record

    async def treat_nlp(, record):
        """
        处理 nlp 信息
        :param record:
        :return:
        """
        label = record.get('label')  # 标签
        category = record.get('category')  # 分类
        entity = record.get('entity')  # 实体

        nlp_result = None
        if not label and not category and not entity:
            # 调用 nlp 接口生成 nlp 内容
            content = record.get('content')  # 完整内容
            nlp_result = await nlp_transform(content)

        # 如果从请求获取的 nlp 结果，需要进行数据结构的整理
        if nlp_result:
            # 提取一个整理过后的 nlp 对象，包含实体、标签和分类
            nlp_item = extract_nlp_result(nlp_result)
            # 将 nlp 对象的内容添加到当前数据
            record.update(nlp_item)

        # 重新获取实体、标签、分类
        entity = record.get('entity')  # 实体
        label = record.get('label')  # 标签
        category = record.get('category')  # 分类
        # 如果仍然没有 nlp 相关信息，返回错误
        if not label and not category and not entity:
            raise Exception("获取 nlp 结果失败")

        # 将源数据的时间信息添加到 nlp 的每个属性中
        origin_time = record.get('origin_time')
        for attr in entity:
            attr['time'] = origin_time
        for attr in category:
            attr['time'] = origin_time
        for attr in label:
            attr['time'] = origin_time
        return record


class DataProcessorEn(DataProcessor):
    def __init__():
        super().__init__()

    async def treat_abstract(, record):
        """
        处理摘要
        :param record:
        :return:
        """
        abstract = record.get('abstract')  # 摘要

        # 检查摘要
        abstract = check_abstract(abstract)

        # 存入摘要
        record['abstract'] = abstract
        return record

    async def treat_nlp(, record):
        """
        处理 nlp 信息
        :param record:
        :return:
        """
        # 获取实体
        entity = record.get('entity')

        if not entity:
            raise Exception("nlp 结果为空")
        nlp_item = extract_nlp_result(entity)
        record.update(nlp_item)
        entity = record.get('entity')
        if not entity:
            raise Exception("nlp 结果为空")
        # 将源数据的时间信息添加到 nlp 的每个属性中
        origin_time = record.get('origin_time')
        for attr in entity:
            attr['time'] = origin_time
        return record

    @staticmethod
    def extract_nlp_result(nlp_result):
        """
        将接口生成的 nlp 的结果提取为固定的格式
        :param nlp_result:
        :return:
        """
        nlp_item = {}
        try:
            if nlp_result:
                old_entity_list = nlp_result
                if old_entity_list:
                    entity_set = {entity for entity in old_entity_list if (entity and entity.strip())}
                    if entity_set:
                        entity_dict_list = [{"tag": entity} for entity in entity_set]
                        nlp_item['entity'] = entity_dict_list
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error(str(e))
        return nlp_item


def get_data_processor(language_type=""):
    """
    根据语言类型返回特定的实例
    :param language_type:
    :return:
    """
    if language_type == "en":
        data_processor = DataProcessorEn()
    else:
        data_processor = DataProcessor()
    return data_processor
