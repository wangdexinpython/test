# -*- coding: utf-8 -*-
import traceback,requests,json
from loguru import logger

url = "http://39.98.194.203:8997/nlp_v2"
data = {"content":"同时也把区块链应用中访问上一代主流区块链更理想的一种方式加进去，我们就看到下面这样的图：两者何等的相似？结合互联网的架构，相信很多聪明的读者朋友会从这相似性一下子就豁然开朗，理解了区块链网络的架构应该是什么，以及去中心化应用在这个体系内的地位。其实不必惊讶，类似的相似性在计算机技术的发展过程中是一而再、再而三地重复出现的。今天互联网的架构也和过去的电信网有着很多的相似之处。技术的发展总是螺旋曲折地稳步前进，因此，当我们今天看到一项大肆宣传的新技术凭空搭建了一个彻头彻尾革新的架构时，反而要多加小心，考察其是否「靠谱」。织链为网：链网成为区块链技术主流进入 2019 年，区块链网络架构在区块链领域崭露头角，ArcBlock、Cosmos （原 Tendermint）和 Polkadot 是目前支持链网架构姿态最明确的几个团队。从上图 ArcBlock、Cosmos 和 Polkadot 技术对比图可见，这三家产品的最大特点就是「织链成网」。我们相信，当越来越多人理解了区块链的架构后，大部分团队可能都会采用这样的架构，或者成为架构里的生态一环。目前，ArcBlock 的链网和 Cosmos 主网相继在 2019 年第一季度发布，均已宣布可以支持无限条链的自由组网，Polkadot 迄今发布了几个测试版本，其官方博客宣布今年第三季度将发布第一版能支持高达 100 条链左右的链网（而之前的白皮书表示支持数百条链），并在 2020 年开始第二版发布后才能支持更多的链加入。演进的启示：从电信网到互联网，再到区块链网络图：电信网到互联网 , 互联网到链网直到今天，互联网并没有完全取代电信网，虽然在大众心目中，互联网的价值和重要性已经远远大于电信网。不过，仅仅就在十几、二十年前，互联网在大多数电信运营商眼里不过是一项「增值数据业务」。"}
cons = requests.post(url,data=data).text
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
        print("nlp_result",nlp_result)
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



ss = extract_nlp_result(json.loads(cons))
print(ss)

