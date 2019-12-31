import requests,re
from lxml import etree
url = 'http://m.39yst.com/yaopin/67390/explain/'
# url = 'http://m.39yst.com/yaopin/67395/explain/'
selector = etree.HTML(requests.get(url).text)

cons = selector.xpath("//section[@class='medicines_explain']//text()")
data = ''.join(cons).replace('\n','').replace(' ','')
adv=re.findall('不良反应】(.*?)【',data)

print(adv)

