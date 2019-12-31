import pymongo,urllib,re
from pymongo import MongoClient
from urllib import parse

def mongodb():
    client = MongoClient(
        "mongodb://topic:" + urllib.parse.quote_plus("Toic7364bfavc78aTp") + "@172.26.26.136:20388/topic")

    # mongo = pymongo.MongoClient(
    #     "mongodb://:topic" + urllib.parse.quote_plus("Toic7364bfavc78aTp")+"@172.26.26.136:20388/topic")['topic']
    return client
mon = mongodb()
ss=mon.topic.AI_topic.find({}).count()
print("数据量",ss)
zds = mon.topic.AI_topic.find_one({})
print("zds",zds)

