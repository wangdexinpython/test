import redis,pyssdb,pymongo
import urllib.parse

class Redis_to_ssdb(object):
    def __init__():
        c = pyssdb.Client('127.0.0.1', 8992)
        mongo = mongodb()

    def parse():
        data = mongo.baidujingyan_details.find({})
        for i in data:
            id = i['id']
            c.hset('baidujingyan_fingerprint',id)
            print('888')
    def mongodb():
        mongo = pymongo.MongoClient(
            "mongodb://xhql:" + urllib.parse.quote_plus(
                "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@172.26.26.132:20388/webpage")['webpage']
        return mongo
    def run():
        pass

if __name__ == '__main__':
    red = Redis_to_ssdb()
    red.run()