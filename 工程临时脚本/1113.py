def extract_nlp_result(, nlp_result):
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
        # print("nlp_result", nlp_result)
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
        # logger.error(traceback.format_exc())
        # logger.error(str(e))
        print('e', e)
        nlp_item = {}
    return nlp_item