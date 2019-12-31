# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidubaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    content_html = scrapy.Field()
    content_np = scrapy.Field()
    web_date = scrapy.Field()
    article_url = scrapy.Field()
    crawl_time = scrapy.Field()
    release_date = scrapy.Field()
    site_name = scrapy.Field()
    image_url = scrapy.Field()
    author = scrapy.Field()
    type = scrapy.Field()
    source = scrapy.Field()
    label = scrapy.Field()
    state_save = scrapy.Field()
    state_segment = scrapy.Field()
    state_label = scrapy.Field()
    state_entity = scrapy.Field()
    state_type = scrapy.Field()
    sign = scrapy.Field()
    state_qiu = scrapy.Field()
    state_qiniu = scrapy.Field()

    # pass
# data = {
#                 "id": id,
#                 "title": title,
#                 "content_html": content_html,
#                 "content_np": content_np,
#                 "web_date": web_date,
#                 "article_url": url,
#                 "crawl_time": crawl_time,
#                 "release_date": '',
#                 "site_name": site_name,
#                 "image_url": image_url,
#                 "author": '',
#                 "type": [],
#                 "source": "baidubaike",
#                 "label": label,
#                 "state_save": 0,
#                 "state_segment": 0,
#                 "state_label": 0,
#                 "state_entity": 0,
#                 "state_type": 0,
#                 "sign": 0,
#                 "state_qiu": 0,
#                 "state_qiniu": 1
#             }
