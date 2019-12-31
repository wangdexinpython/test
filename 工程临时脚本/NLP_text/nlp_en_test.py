# -*- coding: utf-8 -*-
# @Time : 2019/12/4 15:21
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : nlp_en_test.py.py
# @Project : test
'''
pp
'''
import requests,json
data = 'That has deferred the tougher work of adding miles of fencing along the zigzagging course of the lower Rio Grande Valley in South Texas, the nation’s busiest corridor for illegal crossings. There, along the winding river’s edge, the land is almost all privately held, and the government would need to obtain it — either via purchases or eminent domain land grabs — before any construction begins'
def nlp_abstract_8209(data):
    data1 = {"content": data}
    url1 = 'http://summary.abuzahbi.com/abstract'
    try:
        cons1 = requests.post(url1, data=data1).text
        return json.loads(cons1,encoding='utf-8')
    except:
        return json.dumps({})
def nlp_keyword_8209(data):
    data1 = {"content": data}
    url1 = 'http://summary.abuzahbi.com/keywords'
    try:
        cons1 = requests.post(url1, data=data1).text
        return json.loads(cons1,encoding='utf-8')
    except:
        return json.dumps({})

m1 = nlp_abstract_8209(data)
m2=nlp_keyword_8209(data)
print(m1)
print(m2)









