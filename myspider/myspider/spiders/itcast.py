# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(, response):
        # temp = response.xpath("//div[@class='tea_con']/div/ul/li//h3/text()").extract()
        # print(temp)
        li_list = response.xpath("//div[@class='tea_con']/div/ul/li")
        # print(li_list.extract())
        for li in li_list:
            item = {}
            item["name"]=li.xpath(".//h3/text()").extract_first()
            print(item["name"])
            # item["title"]=li.xpath(".//h4/text()").extract_first()
            # item["profile"]=li.xpath(".//p/text()").extract_first()
            # item["come_from"]="itcast"
            # # print(item)
            # logger.warning(item)
            # yield item