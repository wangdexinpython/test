# -*- coding: utf-8 -*-
# @Time : 2019/12/13 15:22
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : ai_topic_webpage.py
# @Project : test

import pymongo,json,re,time
import urllib.parse
from bson.objectid import  ObjectId

def mongodb():
    mongo = pymongo.MongoClient(
        "mongodb://topic:" + urllib.parse.quote_plus("Toic7364bfavc78aTp") + "@172.26.26.136:20388/topic")['topic']
    return mongo
def mongodb2():
    mongo = pymongo.MongoClient(
        "mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@172.26.26.132:20388/webpage")['webpage']
    return mongo
mon_topic=mongodb()
mon_webpage=mongodb2()

num=mon_topic.AI_topic.find({}).count()
for id in range(0,num,1000):
    num1 = mon_topic.AI_topic.find({}).skip(id).limit(1000)
    for k in num1:
        label=k.get("bilstm_label","")
        label_list=label.split(" ")
        k["label"]=label_list
        print(k)
        mon_webpage.AI_topic.update({"id":k.get("id","")},k,True)

print("end")






