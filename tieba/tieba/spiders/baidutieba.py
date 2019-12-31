# -*- coding: utf-8 -*-
import scrapy


class BaidutiebaSpider(scrapy.Spider):
    name = 'baidutieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%96%97%E9%B1%BCtv&fr=index']

    def parse(, response):
        con = response.xpath("//title/text()")
        print(con)
