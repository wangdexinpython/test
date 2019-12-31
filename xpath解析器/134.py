import requests,re
from lxml import etree
url = 'https://mp.weixin.qq.com/s/sPY5EazTDvCfpCQjOrAyxQ'
cons = requests.get(url).text
# print(cons)
# sel=etree.HTML(cons)
# constent = sel.xpath('//*[@id="js_content"]/p[26]')

constent=re.sub('<[^>]+>','',cons)


print('cons',constent)