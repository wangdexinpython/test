# -*- coding: utf-8 -*-
import requests,re

ss = '套餐和资费也新鲜出炉。'
print('sss',ss.strip('。'))








li1 = ['1','','o']
url = 'https://www.leiphone.com/news/201907/DMjXPrsFuiklqA8s.html'
from lxml import etree
cons = requests.get(url).text
sel = etree.HTML(cons)

cons_list = sel.xpath('//div[@class="lph-article-comView"]//text()')
print('cons_list',cons_list)
def not_empty(s):
    b=s.strip('。')
    return b and b.strip()
li2 = list(filter(not_empty,cons_list))
# print('li2',li2)
cons_last = '。'.join(li2)
print('cons_lat',cons_last)
# for i in cons_list:
#     print('start',i)