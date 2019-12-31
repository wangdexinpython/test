import requests,re,json
from scrapy.selector import Selector
class Ifan(object):
    def __init__():
        url = "https://www.ifanr.com/1241659"
    def parse():
        response = requests.get(url).text
        h4_title = Selector(text=response).xpath('//article[@class="o-single-content__body__content c-article-content s-single-article js-article"]/h4/a/text()').extract()
        count = len(h4_title)
        li_p = []
        for i in range(1,count+1):
            regex = '//article[@class="o-single-content__body__content c-article-content s-single-article js-article"]/h4[{}]/following-sibling::p//text()'.format(str(i))
            h4_p = Selector(text=response).xpath(regex).extract()
            li_p.append(h4_p)
        p_parse(li_p)
    def p_parse(,li_p):
        li_p3 =[]
        print('li_p',li_p)
        for i in range(0,len(li_p)):
            print(len(li_p[i]))
        #     print(len(li_p[i+1]))
            if i ==len(li_p)-1:
                li_p3.append(li_p[i])
            else:
                li_p2 = li_p[i][0:len(li_p[i])-len(li_p[i+1])]
                li_p3.append(li_p2)
        for m in li_p3:
            print(m)
    def run():
        parse()
if __name__ == '__main__':
    ifan = Ifan()
    ifan.run()