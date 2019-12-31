import urllib
from bs4 import BeautifulSoup
from urllib import request
from lxml import etree
html=urllib.request.urlopen('http://www.chinarwzj.com/sjjy/3995.html').read()
soup = BeautifulSoup(html,'lxml')
# sel=etree.HTML(html)
# a_=sel.xpath("//td[@valign='top']/table//font//span//text()")
# content=''.join(a_).replace(' ','').replace('&nbsp;','')
# print(content)
print(soup.prettify())
print(soup.font.string)

