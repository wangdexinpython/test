import requests
# from lxml import etree
# url = 'view-source:https://en.wikipedia.org/wiki/Iraq'
# res = requests.get(url).text
# # print(res)
# # //div[@class='item']//dl[@class='item_classly']//a/@href
# sel = etree.HTML(res)
# result = sel.xpath("//table[contains(@class,'infobox')]/following-sibling::p[1]//text()")
# print(result)

url="http://39.98.232.174:8360/jsearch.htm?&dbglv=1&rewrite=1&cache=0&count=20&maxrrec=1200&maxview=512&nouniq=1&start=0&param=sep_sort:crawl_time|desc|sep_uniq:1|sep_fuzzy:0|sep_dint:1&kw=%20label:(NBA)%20tags:recommend"
cons = requests.get(url).text


print(cons)







