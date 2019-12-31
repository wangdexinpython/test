import requests,re


url='https://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA==&mid=2247486237&idx=1&sn=b5b6f0dac8fdaf939af59ff0c1230108&chksm=fbe9b2d2cc9e3bc4fa3f3953d7becef9838219e8c15ffae8b8d94696dd0e6794336725edf491&scene=27'
cons = requests.get(url).text
print(type(cons))
res=re.compile(r'<code>.*?</code>',re.S).sub('',cons)
print(res)