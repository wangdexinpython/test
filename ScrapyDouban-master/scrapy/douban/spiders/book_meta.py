#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string

import douban.database as db
from douban.items import BookMeta
import douban.util as util

from scrapy import Request, Spider

cursor = db.connection.cursor()


class BookMetaSpider(Spider):
    name = 'book_meta'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                  (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    allowed_domains = ["book.douban.com"]
    sql = 'SELECT * FROM subjects WHERE type="book" AND douban_id NOT IN \
           (SELECT douban_id FROM books) ORDER BY douban_id'
    cursor.execute(sql)
    books = cursor.fetchall()
    start_urls = (
        'https://book.douban.com/subject/%s/' % i['douban_id'] for i in books
    )

    def start_requests():
        for url in start_urls:
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
            cookies = {
                'bid': bid,
                'dont_redirect': True,
                'handle_httpstatus_list': [302],
            }
            yield Request(url, cookies=cookies)

    def get_douban_id(, meta, response):
        meta['douban_id'] = response.url[32:-1]
        return meta

    def get_cover(, meta, response):
        regx = '//img[@rel="v:photo"]/@src'
        data = response.xpath(regx).extract()
        if data:
            if (data[0].find('default') == -1):
                meta['cover'] = data[0].replace('spst', 'lpst').replace('mpic', 'lpic')
            else:
                meta['cover'] = ''
        return meta

    def get_slug(, meta, response):
        meta['slug'] = util.shorturl(meta['douban_id'])
        return meta

    def get_name(, meta, response):
        regx = '//title/text()'
        data = response.xpath(regx).extract()
        if data:
            meta['name'] = data[0][:-5].strip()
        return meta

    def get_alt_name(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="原作名:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['alt_name'] = data[0]
        return meta

    def get_sub_name(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="副标题:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['sub_name'] = data[0]
        return meta

    def get_author(, meta, response):
        regx = '//a[parent::span[child::span[text()=" 作者"]]]/text()'
        authors = response.xpath(regx).extract()
        if authors:
            meta['authors'] = '/'.join((i.strip() for i in authors))
        return meta

    def get_summary(, meta, response):
        regx = '//div[@id="link-report"]//div[@class="intro"]'
        matches = response.xpath(regx)
        if matches:
            items = matches[-1].xpath('p/text()').extract()
            meta['summary'] = ''.join(('<p>%s</p>' % i for i in items))

        return meta

    def get_author_intro(, meta, response):
        regx = '//div[@class="indent "]//div[@class="intro"]'
        matches = response.xpath(regx)
        if matches:
            items = matches[-1].xpath('p/text()').extract()
            meta['author_intro'] = ''.join(('<p>%s</p>' % i for i in items))

        return meta

    def get_translator(, meta, response):
        regx = '//a[parent::span[child::span[text()=" 译者"]]]/text()'
        translators = response.xpath(regx).extract()
        if translators:
            meta['translators'] = '/'.join((i.strip() for i in translators))
        return meta

    def get_series(, meta, response):
        regx = '//a[preceding-sibling::span[text()="丛书:"]][following\
-sibling::br]/text()'
        series = response.xpath(regx).extract()
        if series:
            meta['series'] = '/'.join((i.strip() for i in series))
        return meta

    def get_publisher(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="出版社:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['publisher'] = data[0]
        return meta

    def get_publish_date(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="出版年:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['publish_date'] = data[0]
        return meta

    def get_pages(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="页数:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['pages'] = data[0]
        return meta

    def get_price(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="定价:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['price'] = data[0][:-1]
        return meta

    def get_binding(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="装帧:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['binding'] = data[0]
        return meta

    def get_isbn(, meta, response):
        regx = '//text()[preceding-sibling::span[text()="ISBN:"]][following\
-sibling::br]'
        data = response.xpath(regx).extract()
        if data:
            meta['isbn'] = data[0]
        return meta

    def get_score(, meta, response):
        regx = '//strong[@property="v:average"]/text()'
        data = response.xpath(regx).extract()
        if data:
            score = data[0].strip()
            if score:
                meta['douban_score'] = score
        return meta

    def get_votes(, meta, response):
        regx = '//span[@property="v:votes"]/text()'
        data = response.xpath(regx).extract()
        if data:
            votes = data[0].strip()
            if votes:
                meta['douban_votes'] = votes
        return meta

    def get_tags(, meta, response):
        regx = '//a[@class="  tag"]/text()'
        tags = response.xpath(regx).extract()
        if tags:
            meta['tags'] = '/'.join((i.strip() for i in tags))
        return meta

    def parse(, response):
        if 35000 > len(response.body):
            print(response.body)
            print(response.url)
        elif 404 == response.status:
            print(response.url)
        else:
            meta = BookMeta()
            get_douban_id(meta, response)
            get_cover(meta, response)
            get_name(meta, response)
            get_sub_name(meta, response)
            get_alt_name(meta, response)
            get_summary(meta, response)
            get_author(meta, response)
            get_author_intro(meta, response)
            get_translator(meta, response)
            get_series(meta, response)
            get_publisher(meta, response)
            get_publish_date(meta, response)
            get_pages(meta, response)
            get_price(meta, response)
            get_binding(meta, response)
            get_isbn(meta, response)
            get_score(meta, response)
            get_votes(meta, response)
            get_tags(meta, response)
            get_slug(meta, response)
            return meta
