import requests
from lxml import etree
url = 'https://news.163.com/19/0522/07/EFOURRQH0001875P.html'
cons = requests.get(url).text
sel=etree.HTML(cons)
co = sel.xpath("//div[@class='post_text']//p//text()")
ss = ''.join(co).replace(' ','').replace('\n','')
print(ss)