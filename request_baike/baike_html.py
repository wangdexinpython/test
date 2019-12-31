
import requests
import json
import re
from lxml import etree
class Baike(object):
    def __init__(,*args):
        url = args[0]
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
    def parse():
        html = requests.get(url,headers = headers)
        selector = etree.HTML(html.content)
        title1 = selector.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")[0]
        title2 = selector.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h2/text()")[0]
        summary = ''
        menu = ''
        content=''
        reference=''
        key_word=''
        discuss = ''
        content = selector.xpath("//div[@class='main-content']")
        ass = etree.tostring(content[0], encoding='utf-8', pretty_print=False, method='html')
        print(title)
        bbb = str(ass, encoding="utf-8")
        print(bbb)
        # print(key_)
    def con_strip(,li):
       return ' '.join(li).replace('\n', '').replace(' ', '').replace('\xa0','')

    def parse_html():
        pass
    def run():
        parse()
if __name__ == '__main__':
    ss = "https://baike.baidu.com/item/%E9%87%8C%E6%96%AF%E6%9C%AC%E6%9D%A1%E7%BA%A6"
    baike = Baike(ss)
    baike.run()