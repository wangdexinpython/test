# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.parse
from pymongo import MongoClient

class BaidubaikePipeline(object):
    def process_item(, item, spider):
        # print("zoudaozhege")
        return item
class MongodbPipeline(object):
    def __init__():
        # 创建数据库连接
        # client = MongoClient("127.0.0.1:27017")
        client = MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"@47.92.174.37:20388/webpage")
    def process_item(, item, spider):
        # 将数据写入数据库
        print('将数据写入数据库')
        # print(item)
        # item={'id': 'b7ff60fbd406805d06d5a7febc2814f2', 'title': '田村'}
        client.webpage.baike_details.update({'id':item['id']},item,True)
        return item


# class ChuansongmeSpiderDetailPipeline(object):
#     def process_item(, item, spider):
#         return item
# class MongodbPipeline(object):
#     def __init__():
#         # 创建数据库连接
#         client = MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"@47.92.174.37:20388/webpage")
#     def process_item(, item, spider):
#         # 将数据写入数据库
#         client.webpage.web_detail.update({'id':item['id']},item,True)
#         return item