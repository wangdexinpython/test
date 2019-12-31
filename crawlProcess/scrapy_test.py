import scrapy
from xml.sax.saxutils import escape, unescape
from scrapy.crawler import CrawlerProcess
class TEST(scrapy.Spider):
    name = "test"
    allowed_domain=[]
    def start_requests():
        mls = '1527533'
        username = 'starnberg'
        password = 'sTGbYWm?6WN!'
        url = 'http://images.idx.nwmls.com/imageservice/imagequery.asmx'
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'NWMLS:EverNet/RetrieveImages'
        }
        data_query = '<ImageQuery xmlns="NWMLS:EverNet:ImageQuery:1.0"><Auth><UserId>{username}</UserId><Password>{password}</Password></Auth><Query><ByListingNumber>{mls}</ByListingNumber></Query><Results><Schema>NWMLS:EverNet:ImageData:1.0</Schema></Results></ImageQuery>'.format(
            username=username, password=password, mls=mls)
        query = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><RetrieveImages xmlns="NWMLS:EverNet"><query>{}</query></RetrieveImages></soap:Body></soap:Envelope>'.format(
            escape(data_query))
        yield scrapy.Request(url=url,method="POST",body=query,headers=header,callback=parse)
    def parse(, response):
        print(response)

if __name__ == '__main__':
    test=CrawlerProcess()
    test.crawl(TEST)
    test.start()
