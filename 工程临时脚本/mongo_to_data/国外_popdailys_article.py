import pymongo,time,re,json,urllib.parse,hashlib
from pymongo import MongoClient
class Mongo_to_data(object):
    def __init__():
        client = MongoClient("mongodb://dailypops:" + urllib.parse.quote_plus(
            "1!2@3#aAdD") + "@127.0.0.1:20388/dailypops")
        mydb = client['dailypops']
        mycol = mydb["article"]

        client1 = MongoClient("mongodb://admin:" + urllib.parse.quote_plus(
            "mongo123456") + "@47.105.60.112:27017/admin")
        f = open(r'./article_300.dat','a+',encoding='utf-8')
    def parse():
        num = mycol.find({'nlp_state':1},{'_id':0}).sort([('time_stamp',-1)]).limit(300)
        # print('num',num)
        # for i in range(0,num,10000):
        #     print('i',i)
        # zds = mycol.find({'nlp_state':1},{'_id':0}).skip(i).limit(10000)
        for m in num:
            #print('m',m)
            f.write('{}\n'.format(json.dumps(m, ensure_ascii=False)))
                #items={}
                #title = m.get("title", "")
                #content = m.get("content", "")
                #items['id']=md5_(title)
                #items['title']=m.get("title","")
                #items['content']=m.get("content","")
                #items['url']=m.get("url","")
                #time.sleep(10)
                #print('titile',title)
                #print('con',content)
                #if title == '' or content == '':
                #    pass
                #else:
                    #print('入库')
                #    client1.dailypops.article_NLP.update({'id': items['id']}, items, True)
    def md5_(, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()
if __name__ == '__main__':
    mon = Mongo_to_data()
    mon.parse()
