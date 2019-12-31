import pymongo,urllib.parse,json,hashlib
from pymongo import MongoClient
import time
def parse():
    client = MongoClient("mongodb://dailypops:" + urllib.parse.quote_plus(
        "1!2@3#aAdD") + "@47.92.174.37:20388/dailypops")
    mydb = client['dailypops']
    mycol = mydb["article_NLP"]
    return mycol
client = parse()


def md5_(str):
    md5 = hashlib.md5()
    data = str
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()
def read():
    with open(r'./article.dat','r',encoding='utf-8') as f:
        # data = f.readlines()
        # print("len",len(data))
        for da in f:
            # print('da',da)
            try:
                m = json.loads(da)
            except:
                m={"title":"",'content':'','url':''}
                # print("ss",e)
            items = {}
            title = m.get("title", "")
            content = m.get("content", "")
            items['id'] = md5_(title)
            items['title'] = m.get("title", "")
            items['content'] = m.get("content", "")
            items['url'] = m.get("url", "")
            if title == '' or content == '':
                pass
            else:
                print('入库')
                try:
                    client.update({'id': items['id']}, items, True)
                except:
                    pass
read()

