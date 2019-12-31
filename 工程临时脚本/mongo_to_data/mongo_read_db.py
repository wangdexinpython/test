import pymongo,time,re,json,urllib.parse,hashlib,csv
from pymongo import MongoClient
class Mongo_to_data(object):
    def __init__():
        client1 = MongoClient("mongodb://dailypops:" + urllib.parse.quote_plus(
            "1!2@3#aAdD") + "@47.92.174.37:20388/dailypops_cn")['dailypops_cn']
        f = open(r'./article_test.txt','a+',encoding='utf-8')
    def parse():
        num = client1.article_cn.find().count()
        print('num',num)
        for i in range(0,num,3000):
            print('i',i)
            zds = client1.article_cn.find({}).skip(i).limit(3000)
            for m in zds:
                # print('m',m.get("title",""))
                items={}
                items['title']=m.get("title", "")
                items['content']=m.get("content", "")
                items['summary']=m.get("summary","")
                items['label']=m.get("label","")
                f.write('{}\n'.format(json.dumps(items, ensure_ascii=False)))
                # print(items)
                # csv_to(items)
                # client1.dailypops.article_NLP.update({'id': items['id']}, items, True)

    def csv_to(,data):
        lis = [data]
        headers = ['title', 'content']
        with open('./article.csv', 'a', encoding='utf-8', newline='') as f:
            f_scv = csv.DictWriter(f, headers)
            # f_scv.writeheader()
            f_scv.writerows(lis)

    def md5_(, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()
if __name__ == '__main__':
    mon = Mongo_to_data()
    mon.parse()
