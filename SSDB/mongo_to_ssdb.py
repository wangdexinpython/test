#coding=utf-8
import pymongo,pyssdb
import urllib.parse
c = pyssdb.Client(host='172.26.26.133',port=8992)
def mongodb():
    mongo = pymongo.MongoClient(
        "mongodb://xhql:" + urllib.parse.quote_plus(
            "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@172.26.26.132:20388/webpage")['webpage']
    return mongo
mongo = mongodb()
def mongo_to_ssdb():
    count = mongo.query.find({}).count()
    for i in range(0,count,20000):
        print('i',i)
        zds = mongo.query.find().limit(20000).skip(i)
        for k in zds:
            id = k.get("id","")
            sta = hash_exist(id).decode('utf-8')
            if sta=='0':
                hash_(id)
            else:
                print('指纹重复')
            # print(sta)
            # print(i)
def hash_(str):
    return c.hset("query_fingerprint",str,1)
def hash_exist(str):
    return c.hexists('query_fingerprint',str)
if __name__ == '__main__':
    mongo_to_ssdb()
