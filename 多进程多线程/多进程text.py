import threading
import time,pymongo,urllib
import urllib.parse
class Begin(object):
    def __init__():
        mongo = pymongo.MongoClient(
            "mongodb://xhql:" + urllib.parse.quote_plus(
                "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")['webpage']
        f = open(r'./baike_qa.dat', 'a', encoding='utf-8')
    def parse():
        webnum = mongo.baike_qa.find({'state_nlp': {'$exists': False}}).limit(1000)
        for i in webnum:
            # time.sleep(1)
            print(i)
            id = i.get("id")
            title = i.get("title", "")
            title_content = i.get("title_content", "")
            source = i.get("source", "")
            site_name = i.get("site_name", "")
            label = ' '.join(i.get("label", ""))
            type = ' '.join(i.get("type", ""))
            basicInfo = i.get("basicInfo", "")
            ans_and_ques = i.get("ans_and_ques", "")
            # print('111')
            s1 = threading.Thread(target=parse1,args=('s1','s11'))
            s2 = threading.Thread(target=parse2,args=('s2','s22'))
            s3 = threading.Thread(target=parse3,args=('s3','s33'))
            s1.start()
            s2.start()
            s3.start()
    def parse1(,da,dd):
        time.sleep(3)
        print('parse1',da)
        print('parse11',dd)

    def parse2(,dat,dd):
        time.sleep(3)
        print('parse2',dat)
        print('parse22',dd)

    def parse3(,da,dd):
        time.sleep(3)
        print('parse3',da)
        print('parse33',dd)

if __name__ == '__main__':
    be = Begin()
    be.parse()
    # t1 = threading.Thread(target=be.parse1)
    # t2 = threading.Thread(target=be.parse2)
    # t3 = threading.Thread(target=be.parse3)
    # t1.start()
    # t2.start()
    # t3.start()