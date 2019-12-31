import pymongo,re,json,urllib.parse
from pymongo import MongoClient
class text_mongo(object):
    def __init__():
        client1 = MongoClient("mongodb://admin:" + urllib.parse.quote_plus(
            "mongo123456") + "@47.105.60.112:27017/admin")
    def parse():
        client1.dailypops.article_nlp.insert({"1111":"22222"})

if __name__ == '__main__':
    te = text_mongo()
    te.parse()