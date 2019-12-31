import time,scrapy,hashlib
from selenium import webdriver
from lxml import etree
from scrapy.selector import Selector
from database.mongodb import MongoDB

from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument('--headless')


from items import eventItem,articleItem,hotwordItem,questionItem
from selenium.common.exceptions import TimeoutException
from scrapy.crawler import CrawlerProcess
# driver = webdriver.Firefox()
environment='local'
db_name='dailypops'
# class Question(scrapy.Spider):
#     name = 'question'
#     allowed_domain=[]
#     custom_settings = {
#         'LOG_LEVEL': 'ERROR',
#         'CONCURRENT_REQUESTS': 1,
#         'DOWNLOAD_DELAY': 0.2,
#         'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
#         'ITEM_PIPELINES': {'pipeline.pipeline.MongodbPipeline': 300},
#         'DOWNLOADER_MIDDLEWARES': {'middleware.middlewares.GoogleMiddleware': 400}
#     }
#
#     def start_requests():
#         # while True:
#         #     time.sleep(6)
#         url="https://www.google.com/search?biw=1536&bih=890&ei=ZomJXceaOtCbmAWyi7egCg&q={}&oq=commp&gs_l=psy-ab.3.1.0i67l3j0i10l7.8182.9766..12758...0.0..0.135.565.0j5......0....1..gws-wiz.......0.KfvdJE90Egw"
#         client = MongoDB(environment=environment,db_name=db_name).client
#         zds = client.dailypops.hotword.find({"question_state": 0}).limit(4)
#         for k in zds:
#             print('参数',k)
#             hotword = k.get("hotword","")
#             hotword_id=k.get("hotword_id","")
#             event_id=k.get("event_id","")
#             hotword = hotword.split(" ")
#             parms = '+'.join(hotword)
#             # parms = 'competition'
#             url = url.format(parms)
#             url_ = url.format(parms)
#             yield scrapy.Request(url=url_,callback=parse,meta={'hotword_id':hotword_id,'event_id':event_id})
#     def parse(,response):
#         items=questionItem()
#         print('res',response.url)
#         titles = response.xpath('//div[@class="match-mod-horizontal-padding hide-focus-ring cbphWd"]/text()').extract()
#         hotword_id=response.meta.get("hotword_id","")
#         event_id=response.meta.get("event_id","")
#         contents = response.xpath('//div[@class="mod"]').extract()
#         # print(contents)
#         s1 = {'hotword_id': hotword_id}
#         s2 = {'$set': {'question_state': 1}}
#         client.dailypops.hotword.update(s1, s2)
#         for title,content in zip(titles,contents):
#             con = Selector(text=content).xpath('.//text()').extract()
#             con = ''.join(con)
#             items['question_id']=md5_(title+hotword_id)
#             items['event_id']=event_id
#             items['hotword_id']=hotword_id
#             items['question']=title
#             items['answer']=con
#             items['source']=''
#             items['release_time']='2019-09-24'
#             items['time_stamp']=int(time.time())
#             items['entity']=[]
#             items['label']=[]
#             items['static_page']=0
#             items['nlp_state']=0
#             yield items
#     def md5_(, str):
#         md5 = hashlib.md5()
#         data = str
#         md5.update(data.encode('utf-8'))
#         return md5.hexdigest()
# if __name__ == '__main__':
#     process=CrawlerProcess()
#     process.crawl(Question)
#     process.start()

def search():
    client = MongoDB(environment=environment,db_name=db_name).client
    zds = client.dailypops.hotword.find({"question_state": 0}).limit(1000)
    # driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()
    path = r'C:\Users\EDZ\Documents\WeChat Files\wodexinwolai\FileStorage\File\2019-05/chromedriver'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
    begin_url = "https://www.google.com/"
    driver.get(begin_url)
    driver.find_element_by_id("gb_70").click()
    driver.find_element_by_id("identifierId").send_keys("wangxinjie180@gmail.com")
    driver.find_element_by_id("identifierNext").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@name='password']").send_keys("jiexin88")
    driver.find_element_by_id("passwordNext").click()
    time.sleep(5)
    for k in zds:
        # url = 'https://www.google.com/search?sxsrf=ACYBGNRgCAf2dRIVd6dwrtD4B82G2GPK7A%3A1569392173168&ei=LQaLXe35CcmmmAX5k50o&q=trump&oq={}&gs_l=psy-ab.3..35i39l2j0i131j0i3j0i131j0j0i3j0i131l2j0.4634.7621..8636...1.2..3.398.1517.0j7j1j1......0....1..gws-wiz.....10..0i71j0i67j0i131i67j35i362i39j0i131i273j0i273.jn_vf2Z0qbo&ved=0ahUKEwitxPq3qevkAhVJE6YKHflJBwUQ4dUDCAs&uact=5'
        url = "https://www.google.com/search?biw=1536&bih=890&ei=ZomJXceaOtCbmAWyi7egCg&q={}&oq=commp&gs_l=psy-ab.3.1.0i67l3j0i10l7.8182.9766..12758...0.0..0.135.565.0j5......0....1..gws-wiz.......0.KfvdJE90Egw"
        print('参数', k)
        hotword = k.get("hotword","")
        hotword_id=k.get("hotword_id","")
        event_id=k.get("event_id","")
        hotword = hotword.split(" ")
        print('hotword_list',hotword)
        parms = '+'.join(hotword)
        # parms = 'competition'
        print('parms',parms)
        url = url.format(parms)
        # url_ = url.format(parms)

        print('url_',url)
        driver.get(url)
        # driver.find_element_by_class_name("related-question-pair").click()
        response = driver.page_source
        # print(response)
        html = etree.HTML(response)
        titles = html.xpath('//div[@class="related-question-pair"]//div[@class="match-mod-horizontal-padding hide-focus-ring cbphWd"]//text()')
        print('titles',titles)
        contents = Selector(text=response).xpath('//div[@class="related-question-pair"]//div[@class="gy6Qzb kno-ahide"]').extract()
        for title,content in zip(titles,contents):
            con = Selector(text=content).xpath('//div[contains(@class,"mod")]//text()').extract()
            con = ' '.join(con)
            items={}
            items['question_id'] = md5_(title + hotword_id)
            items['event_id']=event_id
            items['hotword_id']=hotword_id
            items['question']=title
            items['answer']=con
            items['source']=''
            items['release_time']='2019-09-25'
            items['time_stamp']=int(time.time())
            items['entity']=[]
            items['label']=[]
            items['static_page']=0
            items['nlp_state']=0
            print(items)
            client.dailypops.question.update({'question_id': items['question_id']}, items, True)
        s1 = {'hotword_id': hotword_id}
        s2 = {'$set': {'question_state': 1}}
        client.dailypops.hotword.update(s1, s2)
        time.sleep(3)

def md5_(str):
    md5 = hashlib.md5()
    data = str
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()
search()






