
import requests,hashlib,datetime
import json
from urllib.parse import urlparse
import re
from lxml import etree
from haxitag.database.mongodb.mongodb import mongo_begin
# students.insert(data)
class BAIKE(object):
    def __init__(,*args):
        url = args[0].decode()
        db_ = args[1]
        coll = args[2]
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }

        connection = mongo_begin().get_collection(coll)
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"
        proxyUser = "HK7PDG1295J2407D"
        proxyPass = "A0D7F8443FA69296"
        proxyMeta = "https://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }
        proxies = {
            "https": proxyMeta
        }
        run()
    def parse():
        html = requests.get(url,headers = headers)
        con = html.headers
        data_time = json.loads(json.dumps(dict(con)))

        selector = etree.HTML(html.content)
        title = selector.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")
        content = selector.xpath("//div[@class='main-content']")
        image_ = selector.xpath("//div[@class='main-content']//img/@data-src")
        print(image_)
        if content != []:
            ass = etree.tostring(content[0], encoding='utf-8', pretty_print=False, method='html')
            print(title)
            bbb = str(ass, encoding="utf-8")
            # print(bbb)
            id_md5 = md5_(url)
            crawl_time = datetime.datetime.now().strftime('%Y/%m/%d')
            site_name =urlparse(url).netloc
            data = {
                "id":id_md5,
                "title":title[0],
                "content":bbb,
                "web_date":data_time["Date"],
                "article_url":url,
                "crawl_time":crawl_time,
                "site_name":site_name,
                "image_url":image_,
                "state_1":0,
                "state_2":0
            }
            sta1 = re.findall('force=',url)
            # print(sta1)
            if sta1 ==[]:
                connection.insert_one(data)
        # print(key_)
    # def con_strip(,li):
    #    return ' '.join(li).replace('\n', '').replace(' ', '').replace('\xa0','')

    def parse_html():
        pass

    def md5_(,str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()
    def run():

        parse()
if __name__ == '__main__':
    ss = "https://baike.baidu.com/item/%E4%B9%9D%E5%B7%9E/6127"
    baike = BAIKE(ss)
    baike.run()