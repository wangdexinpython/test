from .toutiao_re import handle
import requests
url='https://www.cnblogs.com/jim0816/p/9638657.html'
cons = requests.get(url).text

# print(cons.replace(' ',''))