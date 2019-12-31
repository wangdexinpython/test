# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def process_item(, item, spider):
        if item["come_from"] == "itcast":
            item["hello"] = "world"
        return item

# class MyspiderPipeline2(object):
#     def process_item(, item, spider):
#         if item["come_from"] == "itcast1":
#             print(item)
#         return item