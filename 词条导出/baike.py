import pymongo,pymysql,time
import urllib.parse,json
def mongodb():
    # mongo = pymongo.MongoClient("127.0.0.1:27017")
    mongo = pymongo.MongoClient(
        "mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"@47.92.174.37:20388/webpage")['webpage']
    return mongo
mongo = mongodb()
f = open(r'./baike.txt','a+',encoding='utf-8')
def baike():
    webnum = mongo.baike_details.find({}).limit(200000).skip(20000)
    for i in webnum:
        print(i['title'])
        title = i['title']
        f.write(title)
        f.write('\n')
baike()