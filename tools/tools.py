
from lxml import etree
import requests,re
url = 'http://tool.oschina.net/commons'
def requestss():
    cons = requests.get(url).text
    selector = etree.HTML(cons)
    title1 =  selector.xpath("//td[@class='separateColor']/text()")
    print(title1)
    title2=selector.xpath("//td[@class='separateColor']/following-sibling::td[1]/text()")
    jsons={}
    for i,j in zip(title1,title2):
        # print(i)
        if j in jsons:
            if type(jsons[j])==list:
                a = jsons[j]
                a.append(i)
                jsons[j]=a
            else:
                b=jsons[j]
                jsons[j]=[b]
        else:
            jsons[j]=i
    print(jsons)
requestss()