# -*- coding: utf-8 -*-
# @Time : 2019/12/6 11:30
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : list_sort1.py
# @Project : test
'''
pp
'''
from functools import reduce
# ids = ['1','4','3','3','4','2','3','4','5','6','1','9']
# news_ids = []
# for id in ids:
#     if id not in news_ids:
#         news_ids.append(id)
# print (news_ids)
# func = lambda x,y:x if y in x else x+[y]
# ss = reduce(func,[[],]+ids)
# print(ss)

ids="* 田晓萌 杜威 李明 ABC 王建平 BAT 孙云丰 张玉睿 希腊文 京东 李健 哈佛大学 奥地利 侯建斌 于清华 广度 维基百科 AB KPI 波普尔 清华 美国 ROI 孙子 北大 薛兆丰 中国 俞军 微信公众号后台 戴维·巴斯 斯蒂芬·罗宾斯 《认知心理学及其启示》 认知心理学及其启示 美国教育资助委员会 《新制度经济学:一个交易费用分析范式》 新制度经济学:一个交易费用分析范式 《现代制度经济学》 现代制度经济学 《第一本经济学》 第一本经济学 《思维与决策》 思维与决策 《社会心理学》 社会心理学 乔纳森·巴伦 利昂·希夫曼 高少星 埃略特·阿伦森 《俞军产品方法论》 俞军产品方法论 彼得·法乔恩 戴维·谢弗 尼尔·布朗 《博弈与社会》 博弈与社会 埃里克·弗鲁博顿 斯图尔特·基利 《自私的基因》 自私的基因 李明远 丹尼尔·卡尼曼 《消费者行为学》 消费者行为学 《“错误”的行为》 “错误”的行为 鲁道夫·芮切特 查德·泰勒 罗伯特·墨菲 《学会提问》 学会提问 《沟通的艺术:看入人里，看出人外》 沟通的艺术:看入人里，看出人外 《漫谈产品经理》 漫谈产品经理 Baidu.com 《摩登时代》 摩登时代 《经济学原理:微观经济学分册》 经济学原理:微观经济学分册 约翰·安德森 《进化心理学》 进化心理学 《思考，快与慢》 思考，快与慢 基思·斯坦诺维奇 《组织行为学》 组织行为学 苏格拉 《发展心理学:儿童与青少年》 发展心理学:儿童与青少年 《薛兆丰经济学讲义》 薛兆丰经济学讲义 《超越智商》 超越智商 批判性 产品经理 专业能力 用户价值 用户模型 高阶产品 互联网产品经理 能力素质模型 产品管理 产品价值 用户研究 产品迭代 用户分析 招聘体系 工作选择 认知过程 经济学"
ids_encode=ids.encode()
len_1 = len(ids.encode())
print(type(ids.encode()))
id2=ids_encode[0:1024]
print(id2)
id2_spilt=id2.split(b" ")[0:-1]
print('joinssss',type(id2_spilt))
so = b' '.join(id2_spilt)
print(type(so))
# str_byts=' '.join(id2_spilt)
# ss_bytes = bytes(str_byts)
# print("type",type(ss_bytes))


print("len_id2",len(id2))
print(len_1)
# print("id22222",id2.decode())


ss="*"
s1111=" "
print("len_ss",len(ss.encode()))
print(len(s1111.encode()))


print(len(ids))






