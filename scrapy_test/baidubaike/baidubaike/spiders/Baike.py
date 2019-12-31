# -*- coding: utf-8 -*-
import datetime
import hashlib,time,sys,os
import json
sys.path.append(os.path.dirname(__file__)+"/../../")
sys.path.append("../../")
from urllib.parse import urlparse
import scrapy,redis
from lxml import etree
from ..items import BaidubaikeItem
class BaikeSpider(scrapy.Spider):
    name = 'Baike'
    # allowed_domains = ['baike.com']
    # start_urls = ['http://baike.com/']


    def start_requests():
        pool = redis.ConnectionPool(host='47.92.73.83', port=8991, db=2,password='28JCi*289V92ofj2owoBkv8282928SKVISmv8920565LjhMcs')
        # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
        r = redis.Redis(connection_pool=pool)
        while True:
            time.sleep(0.2)
            url = r.lpop('baike_seeds').decode(encoding="utf-8")
            yield scrapy.Request(url, callback=parse_details)
    def parse_details(,response):

        baiduitem = BaidubaikeItem()
        title = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()").extract_first()
        content_html = response.xpath("//div[@class='main-content']/*").extract()
        content_ht = ''
        for i in content_html:
            content_ht+=i
        div = response.xpath("//div[@class='main-content']//div[@class='para']//text()").extract()
        content_np = ''.join(div).replace('\n','').replace(' ','')
        image_ = response.xpath("//div[@class='main-content']//img/@data-src").extract()
        id_md5 = md5_(response.url)
        web_date = response.headers['Date'].decode(encoding = "utf-8")
        labe =response.xpath("//dd[@id='open-tag-item']/span/text()").extract()
        label = []
        for i in labe:
            st = i.replace('\n', '')
            if st != '':
                label.append(st)
        crawl_time = int(time.time())
        article_url = response.url
        site_name = urlparse(response.url).netloc
        baiduitem['id'] = id_md5
        baiduitem['title'] = title
        baiduitem['content_html'] = content_ht
        baiduitem['content_np'] = content_np
        baiduitem['web_date'] = web_date
        baiduitem['article_url'] = article_url
        baiduitem['crawl_time'] = crawl_time
        baiduitem['release_date'] = ''
        baiduitem['site_name'] = site_name
        baiduitem['image_url'] = image_
        baiduitem['author'] = ''
        baiduitem['type'] = []
        baiduitem['source'] = ''
        baiduitem['label'] = label
        baiduitem['state_save'] = 0
        baiduitem['state_segment'] = 0
        baiduitem['state_label'] = 0
        baiduitem['state_entity'] = 0
        baiduitem['state_type'] = 0
        baiduitem['sign'] = 0
        baiduitem['state_qiu'] = 0
        baiduitem['state_qiniu'] = 1

        yield baiduitem
    def parse(, response):
        pass
    def md5_(, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()