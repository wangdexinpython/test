# -*- coding: utf-8 -*-
# @Time : 2019/12/6 14:26
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : ai_topic.py
# @Project : test
'''
pp
'''
import pymongo,json,re,time
import urllib.parse
from bson.objectid import  ObjectId

def mongodb():
    mongo = pymongo.MongoClient(
        "mongodb://topic:" + urllib.parse.quote_plus("Toic7364bfavc78aTp") + "@172.26.26.136:20388/topic")['topic']
    return mongo

f = open(r'./guo_data2.dat', 'a', encoding='utf-8')
mon=mongodb()
s0=mon.AI_topic.find({}).count()
print("count",s0)



