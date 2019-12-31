import pymongo,time,json
from pymongo import MongoClient
import urllib.parse
class Mong(object):
    def __init__():
        client = MongoClient("mongodb://integrate:" + urllib.parse.quote_plus(
            "integ_190228_snv738v8220aiVK9V820@_eate") + "@172.26.26.132:20388/integrate")
    def parse(,dic):
        print(dic['id'])
        client.integrate.data_dat.update({'id': dic['id']}, dic, True)
        print('ok')
    def read_dat(,line):
        if line['topic']=='ai':
            dict_1={'id':line['id'],'content':line['content'],'crawl_time':line['crawl_time'],'title':line['title'],'source':line['source'],'topic':line['topic'],'type':line['type'],'url':line['article_url']}
            try:
                dict_1['label']=line['label']
            except:
                dict_1['label']=''
            # print(dict_1)
            client.integrate.data_dat.update({'id': dict_1['id']}, dict_1, True)
    def run():
        read_dat()
if __name__ == '__main__':
    mong = Mong()
    mong.run()
