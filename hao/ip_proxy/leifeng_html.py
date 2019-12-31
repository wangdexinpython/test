
import requests,re
from lxml import etree
def parse():
    url = "https://www.leiphone.com/news/201807/UxDOs07NoM42ZMHI.html"
    html = requests.get(url)
    con = html.content


    selector = etree.HTML(con)
    sssss = selector.xpath("//div[@class='lph-article-comView']//p[contains(text(),'相关文章：')]")
    print(sssss)
    cons = selector.xpath("//div[@class='lph-article-comView']//p[contains(text(),'相关文章：')]/preceding-sibling::*")
    for i in cons:
        ass = etree.tostring(i,encoding='utf-8', pretty_print=False, method='html')
        ccc = str(ass, encoding="utf-8")
        # print(ccc)
parse()