import requests
from lxml import etree
#
# url = 'https://mp.weixin.qq.com/s?__biz=MjgzMTAwODI0MA==&mid=2651876088&idx=1&sn=1093683f90241ab99636ca87bed03a32&chksm=9b66fc67ac117571040472cf788348e34e09bf720b5bddcf9b9dd845513f6f40382d598bb645&bizpsid=0&scene=126&ascene=3&devicetype=android-27&version=2700043a&nettype=cmnet&abtest_cookie=BAABAAoACwASABMABgBWmR4Ay5keANyZHgDimR4A6JkeAPGZHgAAAA%3D%3D&lang=zh_CN&pass_ticket=AfZcnOCnYo5eSRgmKnP%2F8TIYzswskZjjk4evDOuZhvwNF%2FcLlhjd5yvg2CxEAFXW&wx_header=1'
#
#
# # cons = requests.get(url).text
# url_io = 'http://api.url2io.com/article?token=B2Iv2c4HQPmUEWjSmdMXzQ&url={}&fields=text'.format(url)
#
# cons = requests.get(url_io).text
#
# print(cons)

url = 'https://mp.weixin.qq.com/s/-zI2EpV5YWSdBQwoYkzdMw'
html = etree.HTML(requests.get(url=url).text).xpath('//div[@id="js_content"]/section//text()|//div[@id="js_content"]//p//text()')
content_n = ''.join(html).replace(' ', '').replace('&amp;', '').replace('amp;', '').replace('amp;gt;', '').replace(
    '\n', '').replace('\r', '').replace('\t', '').replace('好看的人都点了在看','')
print(content_n)