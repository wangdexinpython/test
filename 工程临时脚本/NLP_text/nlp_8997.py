# -*- coding: utf-8 -*-

import requests,json


data = '''新智元专栏 作者：@龙星镖局【新智元导读】北京马拉松今天正在如火如荼地跑着，AI在体育产业的应用越来越受到关注。这篇文章是对KDD 2017上一篇《Athlytics：体育运动分析中的数据挖掘与机器学习》的解析，探讨在球类比赛中对数据进行挖掘和分析，提高球队价值的技术手段。论文&PPT：http://www.pitt.edu/~kpele/kdd2017-tutorial.html很早以前看过一部体育题材的电影《点球成金》，英文名MoneyBall。片子讲述了布拉特皮特饰演的球队总经理和耶鲁大学经济系毕业的数据分析师一起通过对棒球比赛数据进行挖掘和分析，淘宝联盟里性价比高、拥有一技之长的球员组队，进而取得成功的光荣事迹。该片充分展现了利用数据来提升球队的价值和意义，令人印象非常深刻。一直想对其中用到的技术手段一探究竟，而KDD 2017上的《Athlytics: Data Mining and Machine Learning for Sports Analytics》这个topic实在是再合适不过了。这个讲座由KonstantinosPelechrinis (University of Pittsburgh)，EvangelosPapalexakis (University of California, Riverside)，Benjamin Alamar (ESPN)三位合作，学术界+工业界的模式保证了实用性。整个topic还是很研究范儿，数学公式比较多，但解决的问题和方法还是相对比较浅。这里可能有两个原因：1.这个领域人们之前并未足够重视，大部分还是依靠专业球探的经验；2. 这个领域价值很大 (权威机构预测到2021年体育数据分析的市场有47亿美金) 更专业更有价值的方法并未公开。具体方法不再一一赘述，挑三个有趣的分享一下，更多可以参考ppt链接。（1）评估球员实力：修正的正负值指标Plus−minus正负值是评估球员实力的主要指标，该指标越高，意味着球员能力越强。以安东尼-5为例，就是安东尼上场的时间内，球队输了5分。但该指标只考虑球员在场的得失分差，明显有很多不合理的地方。比如场上领先时，不代表每个人都对这次的成功合作做出了正面的贡献，退一步讲，即使每个人有正面贡献，贡献少 能力低的也很难通过这种数据被区分出来。如何区分每个球员对胜利的贡献是其中的关键问题，研究者们借助线性模型对每个回合进行回归建模，因变量（DV）是每回合的得分、自变量（IV）则是所有球员，回归的结果就是每个球员会有一个权重，而这个权重代表了球员对胜利贡献。这里自变量的设计很巧妙，针对每一个回合，我方在场球员用1表示，对方在场球员用-1表示，其他球员用0表示，这样起到的一个效果就是本回合的得分和我方在场球员正相关，和对方在场球员负相关，而和不在场球员无关。多个回合经过模型学习后，每个球员都有了自己的一个权重，越大表示这个球员对胜利的贡献越大，同时由于每个回合都考虑我方在场和对方在场的球员，也把其他球员的影响自动考虑进去。上图是NBA 07-08赛季头部和尾部Top5的球员，看起来非常靠谱，和大部分球迷的认知还是比较一致的。（2）预测比赛胜负：基于PageRank的Sportsnetrank简单来说Sportsnetrank基于pagerank的思想，将球队之间的比赛建模成图，结点是球队，边是球队之间的战绩(得失分)。然后在图上运行pagerank，就可以得到每个球队的实力评估分数，pr值越大，球队实力越强，胜率越高。下图是基于NFL联赛构建出来的图，结点越大，球队越强。边越粗，说明球队交手时差距越大。预测比赛胜负时，可以简单根据之前的交手记录构建图，然后计算出每个球队的目前实力。当两个球队交手时，实力更强的球队预测为胜。就是这样一个简单的策略，就能取得很好的效果，按作者的原话是达到了stat-of-the-art的水平。上图是NFL联赛预测的结果和真实的结果的比较，可以看出确实不简单。（3）战术有效性：挡拆识别及评估挡拆(防守)是NBA最常见的战术，也是得分最有效的手段。有研究者建立并实验了一套自动识别常见挡拆防守套路的系统。利用SportVU球员追踪数据和监督式机器学习方法，建立了一套学习分类器，用于分辨防守挡拆的四种方式：“挤过（over）”、“绕过（under）”、“包夹（trap）”、“换防（switch）”。具体含义如下：挤过：持球防守者在持球人和掩护者之间，即从掩护上方挤过；绕过：持球防守者不在持球人和掩护者之间，即从掩护下方绕过；换防：持球防守者和掩护防守者交换防守对象；包夹：持球防守者和掩护防守者夹击持球人。然后作者手动标记了四种类型的若干样本，并进一步训练构建了分类器来发现更多的挡拆。最终识别结果如下：全部270823个挡拆，“挤过”146314个，“绕过”69721个，“换防”37336个，“包夹”17451个。对这些进一步分析可以得到以下一些有趣的结论：各赛季四类挡拆分布基本一致，但可以注意到“包夹”的比例略有提高，说明随着个人得分能力更强后，包夹会越来越多？b. 哪些组合不来电？下图比较了不同防守组合面对挡拆的每回合失分以及他们各自与所有球员搭档的平均每回合失分。克里斯-保罗和布雷克-格里芬是使用挤过的效果是最差的之一，平均失去1.2分。另外伊巴卡和雷吉-杰克逊组合的换防很差，但各自挡拆防守效率很接近。【题外话，如今这两对组合已经都被拆散了，是不是经理看到了这个研究？】结语：AI在体育产业的应用才刚刚开始，还有很多amazing的应用正在展开或者即将展开。感兴趣的同学可以自行搜索相关资料进行学习研究。Slides地址：http://www.pitt.edu/~kpele/kdd2017-tutorial.html【号外】新智元正在进行新一轮招聘，飞往智能宇宙的最美飞船，还有N个座位点击阅读原文可查看职位详情，期待你的加入~"'''
def nlp_get_8997(data):
    data1 = {"text": data}
    url1 = 'http://39.98.194.203:8997/nlp'
    try:
        cons1 = requests.post(url1, data=data1).text
        return cons1
    except:
        return json.dumps({})



def nlp_get_8997_v2(data):
    data1 = {"text": data}
    url1 = 'http://39.98.194.203:8997/nlp_v2'
    try:
        cons1 = requests.post(url1, data=data1).text
        return cons1
    except:
        return json.dumps({})





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
cons = nlp_get_8997_v2(data)
res = extract_nlp_result(json.loads(cons))
print(res)
# m2=nlp_get_8997_v2(data)
# m1 = nlp_get_8997(data)
# print(m1)
# print(m2)


