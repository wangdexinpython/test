import requests,re
from lxml import etree

url = 'http://m.39yst.com//yaopin/c/21/2/'
cons=requests.get(url).text
selec=etree.HTML(cons)
details_dl = selec.xpath("//div[@class='medicines_list_bar']/dl")
print(details_dl)

# ass = etree.tostring(content[0], encoding='utf-8', pretty_print=False, method='html')
# print(title)
# bbb = str(ass, encoding="utf-8")

# for k in details_dl:
#     ass = etree.tostring(k,encoding='utf-8', pretty_print=False, method='html')
#     bbb=str(ass,encoding="utf-8")
#     prices = k.xpath("//dd/label/strong/text()")
#     print(bbb)
#     print(prices)
k=details_dl[0]
ass = etree.tostring(k, encoding='utf-8', pretty_print=False, method='html')
bbb = str(ass, encoding="utf-8")
selector = etree.HTML(bbb)
prices = selector.xpath("//dd/label/strong/text()")
print(bbb)
print(prices)
