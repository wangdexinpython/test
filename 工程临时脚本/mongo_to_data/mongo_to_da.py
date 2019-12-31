import pymongo,time,re,json,urllib.parse,hashlib
from pymongo import MongoClient
class Mongo_to_data(object):
    def __init__():
        client = MongoClient("mongodb://dailypops:" + urllib.parse.quote_plus(
            "1!2@3#aAdD") + "@127.0.0.1:20388/dailypops")
        mydb = client['dailypops']
        mycol = mydb["article"]

        client1 = MongoClient("mongodb://admin:" + urllib.parse.quote_plus(
            "mongo123456") + "@47.105.60.112:20388/admin")
        # f = open(r'./article.dat','a+',encoding='utf-8')
    def parse():
        num = mycol.find().count()
        print('num',num)
        zds = mycol.find({})
        for m in zds:
            print('m',m.get("title",""))
            items={}
            title = items.get("title", "")
            content = items.get("content", "")
            items['id']=md5_(title)
            items['title']=m.get("title","")
            items['content']=m.get("content","")
            items['url']=m.get("url","")
            time.sleep(10)

            if title == '' or content == '':
                pass
            else:
                client1.dailypops.article_NLP.update({'id': id}, items, True)
    def md5_(, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()
if __name__ == '__main__':
    mon = Mongo_to_data()
    mon.parse()







