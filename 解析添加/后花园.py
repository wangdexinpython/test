import json
import requests
from lxml import etree
import re
import chardet
def get_url(url):
    response = requests.get(url=url)
    # print(response)
    response.encoding='utf-8'
    html = etree.HTML(response.text)
    title = html.xpath('//h1[@class="title"]/text()')[0]
    # print(title)
    content = re.findall('<input type="text" id="newsBody" (.*?)/>',response.text)
    content  = str(content).replace('[','').replace(']','')
    content = re.findall('&gt;(.*?)&lt;', content)
    print('content',''.join(content))
    # content = re.findall('&gt;(.*?)&lt;',content) and re.findall('&gt;(.*?)&lt;',content) or ""
    # content1 = ''.join(content)
    # print(title,content1)
if __name__ == '__main__':
    get_url(url='https://nz.hougarden.com/news/article-20190824180047-f813')