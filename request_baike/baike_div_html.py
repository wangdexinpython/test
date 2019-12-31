
import requests
import json
import re
from lxml import etree
class Baike(object):
    def __init__():
        url = 'https://baike.baidu.com/item/%E6%AC%A7%E6%B4%B2%E8%81%94%E7%9B%9F/786749?fromtitle=%E6%AC%A7%E7%9B%9F&fromid=383198'
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
    def parse():
        html = requests.get(url,headers = headers)
        selector = etree.HTML(html.content)
        title = selector.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")[0]
        content = selector.xpath("//div[@class='para']//text()")
        key_con = selector.xpath("//div[@class='basic-info cmn-clearfix']//text()")
        img_con = selector.xpath("")
        con = con_strip(content)
        key_ = con_strip(key_con)
        print(title)
        print(con)
        # print(key_)
    def con_strip(,li):
       return ' '.join(li).replace('\n', '').replace(' ', '').replace('\xa0','')

    def parse_html():
        pass
    def run():
        parse()
if __name__ == '__main__':
    baike = Baike()
    baike.run()