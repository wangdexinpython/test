import requests
from lxml import etree
# # https://mp.weixin.qq.com/s/7vdc_vz8EKZuCeYd-G-2Sw
# article_url = 'https://mp.weixin.qq.com/s/-zI2EpV5YWSdBQwoYkzdMw'
# response = requests.get(url=article_url)
# html = etree.HTML(response.text)
# div = html.xpath('//div[@id="js_content"]//p//text()')
# content_n = ''.join(div)
# content_np = str(content_n).replace(' ', '').replace('&amp;', '').replace('amp;', '').replace('amp;gt;', '').replace(
#     '\n', '').replace('\r', '').replace('\t', '')
# print(content_np)
import re
url = 'https://view.inews.qq.com/a/20190509A03XPQ00?chlid=news_news_top&shareto=wx'
desc = re.findall('"cnt_html":"(.*?)",',requests.get(url).text)
text = desc[0].encode('utf-8').decode('unicode_escape') if desc!=[] else ''
result= re.compile(r'<[^>]+>', re.S).sub('',text).replace('\\','')
print(result)









