from bson.objectid import ObjectId
import pymongo,pymysql,time,requests
import urllib.parse,json
def mongodb():
    mongo = pymongo.MongoClient("127.0.0.1:27017")
    # mongo = pymongo.MongoClient(
    #     "mongodb://integrate:" + urllib.parse.quote_plus("integ_190228_snv738v8220aiVK9V820@_eate")+"@172.26.26.132:20388/integrate")['integrate']
    return mongo
mog = mongodb()
def get_mongo():
    # cur = mys.cursor()
    webnum = mog.contents.find({})
    for one in webnum:
        print(one)
get_mongo()
