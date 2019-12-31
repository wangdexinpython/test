# -*- coding:utf-8 -*-

# from ssdb import SSDB
import hashlib
# try:
#     ssdb = SSDB('39.98.232.174', 8992)
# except Exception as e:
#
#     print(e)
#     # sys.exit(0)
# # ssdb.get()
# # ssdb.set(['test', '123'])
# # ssdb.request('get', ['test'])
# # ssdb.request('incr', ['test', '1'])
# # ssdb.request('decr', ['test', '1'])
# # ssdb.
# # ssdb.set('test',13)
# ssdb.qpush_front('baike3','ss24')
# def parse_redis():
#     pool = redis.ConnectionPool(host='172.26.26.133', port=8991, db=4,password='28JCi*289V92ofj2owoBkv8282928SKVISmv8920565LjhMcs')
#     return redis.Redis(connection_pool=pool)
# import pyssdb
# c = pyssdb.Client('39.98.232.174',8992)
# c = pyssdb.Client('172.26.26.133',8992)
# ss = c.qpop_front('query_seeds')
# print(ss)
# c.set('one','be')
# p =c.get('one')
# print(p)
# c.qpush_front('baike','787878')
# num = c.qsize('query_seeds')
# print(num)
# c.qpush_front('zhidao_seeds',data)
# ss = c.qpop('query_seeds')
# print(ss)
# c.hset(h'jingyan','tsteeg')
# c.hset('h','jingyan','id')
# def md5_(str):
#     md5 = hashlib.md5()
#     data = str
#     md5.update(data.encode('utf-8'))
#     return md5.hexdigest()
# url='http://22606.med.999120.net'
# md5_url=md5_(url)
# ss =c.hexists('med999120_fingerprint',md5_url)
# s0s=ss.decode('utf-8')
# if s0s=='0':
#     print('not')
# print('ssss',s0s)


# import requests,time,re,hashlib,json
# import threading,pyssdb
# import pymongo,urllib.parse,json
# class Get_nlp(object):
#     def __init__():
#         mongo = mongodb()
#         # c = pyssdb.Client(host='172.26.26.133', port=8992)
#     def parse():
#         # while True:
#             # ids=c.qpop_front('weixin_id').decode('utf8')
#         one = mongo.weixin.find({'id':'c2459a5cbb172e920d4e5418c00f6cca'})
#         print(type(one))
#             # dict_mongo(one)
#     def mongodb():
#         mongo = pymongo.MongoClient(
#             "mongodb://xhql:" + urllib.parse.quote_plus(
#                 "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")['webpage']
#         return mongo
#
# if __name__ == '__main__':
#     gg = Get_nlp()
#     gg.parse()
import requests
import json
# ss = 'huhuhuh'
# s1=json.dumps(ss)
# print(s1)
# s1 = json.loads(s1).get('name','')

title='蔡昱峰受聘为第二届中南大学长沙校友会副会长'
content='2019丨1月20日2019年1月20日，中南大学长沙校友会2019迎新年会在长沙茉莉花大酒店顺利举办。中南大学党委常务副书记陶立坚、副校长郭学益、原党委常务副书记徐建军等校领导，中南大学长沙校友总会秘书长张忠生、法学院党委书记王新平、法学院原常务副院长刘继虎等在湘校友，以及异地兄弟校友会欢聚一堂，共叙校友情谊。作为校友，自兴人工智能董事长蔡昱峰先生受邀参加本次活动，并受聘为“第二届中南大学长沙校友会副会长”。▲蔡昱峰（右二）在会上“创新创业分享”环节，蔡昱峰先生还发表了《共创人工智能时代》主题演讲，分享了自兴人工智能的发展历程、获得的荣誉及在AI“产学研”道路上的探索。蔡总认为，当今高速发展的人工智能行业引领着一个变革的时代，也是最好的财富机会点，诚挚邀请各位校友一同强强联手，抓住机遇，脚踏实地，共创人工智能新时代'


def nlp_get_8997(data):
    data1 = {"text": data}
    url1 = 'http://39.98.194.203:8997/nlp'
    try:
        cons1 = requests.post(url1, data=data1).text
        return cons1
    except:
        return json.dumps({})


def nlp_get_8994(data):
    data1 = {"text": data}
    url1 = 'http://39.98.194.203:8994/nlp'
    cons1 = requests.post(url1, data=data1)
    if cons1.status_code == 500:
        cons1 = {}
        return json.dumps(cons1)
    else:
        return cons1.text

def nlp_get_bd_label(title,data):
    label_url = 'http://39.98.194.203:8992/keyword/'
    data_label = {"title":title,"content":data}
    label_data = json.loads(requests.post(label_url,data=data_label).text)
    label_=label_data.get("items","")
    a=[]
    for i in label_:
        b = i.get("tag","")
        a.append(b)
    return ' '.join(a)

ss = nlp_get_8997(content)
s1 = nlp_get_8994(content)
s2 = nlp_get_bd_label(title,content)
print(ss)
print('s1',s1)
print(s2)



