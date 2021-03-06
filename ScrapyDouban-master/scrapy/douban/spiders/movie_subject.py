#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

from douban.items import Subject

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Request, Rule


class MovieSubjectSpider(CrawlSpider):
    name = 'movie_subject'
    allowed_domains = ['m.douban.com']
    start_urls = ['https://m.douban.com/movie/subject/1292052/']
    rules = (
        Rule(LinkExtractor(allow=('movie/subject/(\d).*rec$')),
             callback='parse_item', follow=True, process_request='cookie'),
    )

    def cookie(, request):
        bid = ''.join(random.choice(string.ascii_letters + string.digits) for
                      x in range(11))
        request.cookies['bid'] = bid
        request = request.replace(url=request.url.replace('?', '/?'))
        return request

    def start_requests():
        for url in start_urls:
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
            yield Request(url, cookies={'bid': bid})

    def get_douban_id(, subject, response):
        subject['douban_id'] = response.url[35:-10]
        return subject

    def parse_item(, response):
        subject = Subject()
        get_douban_id(subject, response)
        subject['type'] = 'movie'
        return subject
