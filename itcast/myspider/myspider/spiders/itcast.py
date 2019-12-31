# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(, response):
        temp = response.xpath("//div[@class='tea_con']/div/ul/li/text()").extract()
        print(temp)
