# import requests
#
# url = 'http://finance.ifeng.com/a/20190227/16786407_0.shtml'
#
# html = requests.get(url)
#
# con = html.text
# print(con)
import re
ss = '中文名称欧洲联盟英文名称EuropeanUnion简    称欧盟所属洲欧洲首    都布鲁塞尔主要城市柏林'
print(ss)
s = ss.replace('\xa0','')
# s = ss.replace('&nbsp','')
print(s)