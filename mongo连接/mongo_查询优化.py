# -*- coding: utf-8 -*-
import pyssdb,pymongo,json,time,re,urllib.parse,hashlib
class Query(object):
    def __init__():
        mongo = pymongo.MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@172.26.26.132:20388/webpage")['webpage']
        c=pyssdb.Client(host='172.26.26.133',port=8992)
    def parse():
        coun = mongo.business_zhidao.find({}).limit(30000)
        id_=0
        for i in coun:
            id_ = i.get('_id','')
            id1 = i.get("id","")
            seeds(id1)
        parse_deep(id_)
    def parse_deep(,id_):
        one = mongo.business_zhidao.find({'_id':{'$gt':id_}}).limit(30000)
        id_=0
        for k in one:
            id2 = k.get("id","")
            seeds(id2)
            id_=k.get('_id','')
        parse_deep(id_)


    def seeds(, str):
        c.qpush_front('zhidaoid_seeds', str)
    def run():
        parse()
if __name__ == '__main__':
    query = Query()
    query.run()
