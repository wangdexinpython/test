# -*- coding: utf-8 -*-
import scrapy,hashlib,time,json,re,redis,threading,urllib.parse
from scrapy.crawler import CrawlerProcess
import pymongo
from pymongo import MongoClient
mongo = pymongo.MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")['webpage']
# f1 = open(r'./qa.dat', 'a+', encoding='utf-8')
f2 = open(r'./jb.dat', 'a+', encoding='utf-8')
f3 = open(r'./zz.dat', 'a+', encoding='utf-8')
f4 = open(r'./jy.dat', 'a+', encoding='utf-8')
f5 = open(r'./qw.dat', 'a+', encoding='utf-8')
def read_mongo():
    zds = mongo.medical_qa.find().limit(100).skip(2000)
    for k in zds:
        sym = k.get("problem", "")
        # print(sym)
        parse(sym)
def parse(data):
    print(data)
    parms = input()
    items = {'qa':data,'classify':parms}
    # print(data,parms)
    write_data(items)
def write_data(ite):
    classify = ite.get("classify","")
    if classify=='qa':
        with open(r'./qa.dat', 'a+', encoding='utf-8') as f1:
            da1 = ite.get("qa","")
            f1.write('{}\n'.format(da1))
    elif classify=='jb':
        with open(r'./jb.dat', 'a+', encoding='utf-8') as f2:
            da1 = ite.get("qa", "")
            f2.write('{}\n'.format(da1))
    elif classify=='zz':
        with open(r'./zz.dat', 'a+', encoding='utf-8') as f3:
            da1 = ite.get("qa", "")
            f3.write('{}\n'.format(da1))
    elif classify=='jy':
        with open(r'./jy.dat', 'a+', encoding='utf-8') as f4:
            da1 = ite.get("qa", "")
            f4.write('{}\n'.format(da1))
    elif classify=='qw':
        with open(r'./qw.dat', 'a+', encoding='utf-8') as f5:
            da1 = ite.get("qa", "")
            f5.write('{}\n'.format(da1))
read_mongo()







