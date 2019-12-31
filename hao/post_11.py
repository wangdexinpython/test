import requests,re
from lxml import etree
class pkulaw(object):
    def __init__():
        url = 'https://www.pkulaw.com/law/search/RecordSearch'
        url2 = ''
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Cookie':'pkulaw_v6_sessionid=zzp1ffed34bescmdfaasiuyn; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1555685834; Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1555687664; Porschev=MainSessionId=i1hkdpf2vy15fdrkeemnshgj'
        }
    def parse():
        parms = {}
        parms['Menu']='law'
        parms['SearchKeywordType']='DefaultSearch'
        parms['Library']='chl'
        parms['ClassCodeKey']=',XC02,,,,'
        parms['Pager.PageSize']=10
        parms['Pager.PageIndex']=0
        cons = requests.post(url,data=parms,headers=headers)
        response=etree.HTML(cons.text)
        li_ = response.xpath("//div[@class='list-title']//label[@name='sortNum']/following-sibling::a[1]/@href")
        print(li_)
        for i in li_:
            url = 'https://www.pkulaw.com'+i
            parse_two(url)
    def parse_two(,url):
        cons = requests.get(url,headers=headers).text
        select = etree.HTML(cons)
        text = select.xpath("//div[@id='divFullText']//text()")
        cons = ''.join(text).replace(' ','')
        print(cons)
if __name__ == '__main__':
    pku = pkulaw()
    pku.parse()