import urllib
from urllib import request
from lxml import etree
html=urllib.request.urlopen('http://www.chinarwzj.com/sjjy/3995.html').read()
sel=etree.HTML(html)
a_=sel.xpath("//td[@valign='top']/table//font//span//text()")
content=''.join(a_).replace(' ','').replace('&nbsp;','')
print(content)
