import pymongo,time,json
from pymongo import MongoClient
import urllib.parse
class Mong(object):
    def __init__():
        pass
    def read_dat():
        f1 = open(r'./inc_zhidao_20190520.dat','a', encoding='utf-8')
        with open(r'./inc_zhidao_20190520.dat','r',encoding='utf-8') as f:
            for line in f:
                id1 = line['id']
                line['link']=id1
                f1.write('{}\n'.format(json.dumps(line, ensure_ascii=False)))

if __name__ == '__main__':
    mong = Mong()
    mong.read_dat()



