# -*- coding: utf-8 -*-
# from scrapy_redis.spiders import RedisSpider
import hashlib, time, sys, os, scrapy, redis, json, requests, re
from scrapy.spiders.crawl import Spider
sys.path.append(os.path.dirname(__file__) + "/../../")
sys.path.append("../../")
from urllib.parse import urlparse
from lxml import etree
# from ..items import BaikeItem
class BaikeSpider(scrapy.Spider):
    name = 'Baike'
    redis_key = 'baike_seeds'
    # custom_settings = {
    #     # 指定redis数据库的连接参数
    #     # 'REDIS_HOST': '172.26.26.133',
    #     'REDIS_HOST': '127.0.0.1',
    #     'REDIS_PORT': 6379,
    #     # 指定 redis链接密码，和使用哪一个数据库
    #     'REDIS_PARAMS': {
    #         # 'password': '28JCi*289V92ofj2owoBkv8282928SKVISmv8920565LjhMcs',
    #         'db': 1
    #     },
    # }
    # def __init__(, *args, **kwargs):
    #     super(BaikeSpider, ).__init__(*args, **kwargs)
    def start_requests():
        yield scrapy.Request(callback=parse)
    def parse(, response):
        # baikeitem = BaikeItem()
        title = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()").extract_first()
        div1 = response.xpath("//div[@class='lemma-summary']/div//text()").extract()
        div2 = response.xpath("//div/div[@class='para']//text()").extract()
        div1 = ''.join(div1).replace('\n', '')
        div2 = ''.join(div2).replace('\n', '')
        content_np = div1 + div2
        content_html = response.xpath("//div[@class='main-content']").extract()
        image_ = response.xpath("//div[@class='main-content']//img/@data-src").extract()
        id_md5 = md5_(response.url)
        web_date = response.headers['Date'].decode(encoding="utf-8")
        crawl_time = int(time.time())
        site_name = urlparse(response.url).netloc
        label1 = response.xpath("//dd[@id='open-tag-item']/span/text()").extract()
        label = []
        for i in label1:
            st = i.replace('\n', '').replace(' ', '')
            if st != '':
                label.append(st)
        print(label)
        # baikeitem['id'] = id_md5
        # baikeitem['title'] = title
        # baikeitem['content_html'] = content_html[0] if content_html != [] else ''
        # baikeitem['content_np'] = content_np
        # baikeitem['web_date'] = web_date
        # baikeitem['article_url'] = response.url
        # baikeitem['crawl_time'] = crawl_time
        # baikeitem['release_date'] = ''
        # baikeitem['site_name'] = site_name
        # baikeitem['image_url'] = image_
        # baikeitem['author'] = ''
        # baikeitem['type'] = ''
        # baikeitem['source'] = 'baidubaike'
        # baikeitem['label'] = label
        # baikeitem['state_save'] = 0
        # baikeitem['state_segment'] = 0
        # baikeitem['state_label'] = 0
        # baikeitem['state_entity'] = 0
        # baikeitem['state_type'] = 0
        # baikeitem['sign'] = 0
        # baikeitem['state_qiu'] = 0
        # baikeitem['state_qiniu'] = 1
        # yield baikeitem

    def md5_(, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()
if __name__ == '__main__':
    pass











