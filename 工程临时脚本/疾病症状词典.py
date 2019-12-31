# -*- coding: utf-8 -*-
import scrapy,hashlib,time,json,re,redis,threading,urllib.parse
from scrapy.crawler import CrawlerProcess
import pymongo
from pymongo import MongoClient
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=7)
r = redis.Redis(connection_pool=pool)
fw = open(r'./symptom_unique.txt', 'a+', encoding='utf-8')
mongo = pymongo.MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")['webpage']
def read_txt():
    with open('./symptom.txt','r',encoding='utf-8') as f:
        data = f.readlines()
        for k in data:
            li1 = k.strip().split('\t')
            for m in li1:
                md5_s = md5_(m)
                sta = hash_exist(md5_s)
                # print()
                if sta ==False:
                    fw.write('{}\n'.format(m))
                    hash_(md5_s)
                else:
                    print('指纹重复')
def read_mongo():
    zds = mongo.disease360.find()
    for k in zds:
        sym = k.get("symptom","")
        s1 = sym.split('、')
        for k in s1:
            md5_s = md5_(k)
            sta = hash_exist(md5_s)
            # print()
            if sta == False:
                fw.write('{}\n'.format(k))
                hash_(md5_s)
            else:
                print('指纹重复')
# fw.write('{}\n'.format())

def hash_(str):
    return r.hset(name="symptom_fingerprint", key=str, value=1)
def hash_exist(str):
    return r.hexists(name='symptom_fingerprint',key=str)
def md5_(str):
    md5 = hashlib.md5()
    data = str
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()
# read_txt()
read_mongo()
