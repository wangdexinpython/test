import redis,pymongo,pyssdb
import urllib.parse

class get_redis(object):
    def __init__():
        red = mongodb()
        c=pyssdb.Client(host='172.26.26.133',port=8992)
    def parse():
        webnum = red.baike_details.find({}).count()
        print(webnum)
        for i in range(0, webnum, 30000):
            print('*****************************************', i)
            cons = red.baike_details.find({}).limit(30000).skip(i)
            for j in cons:
                id = j['id']
                c.hset('baike_fingerprint',id,1)
    def mongodb():
        # mongo = pymongo.MongoClient("127.0.0.1:27017")
        mongo = pymongo.MongoClient(
            "mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"@172.26.26.132:20388/webpage")['webpage']
        return mongo
if __name__ == '__main__':
    g = get_redis()
    g.parse()

