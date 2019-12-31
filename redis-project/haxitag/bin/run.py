# -*- coding: utf-8 -*-
import sys,os,urllib
# reload(sys)
# sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(__file__)+"/../../")
sys.path.append("../../")

from haxitag.spiders.baike_details import BAIKE
from haxitag.database.mongodb.mongodb import MongoDB
from pymongo import MongoClient

# connection = MongoDB().client.get_database('baidubaike')
import redis
def parse_redis():
    try:
        # host is the redis host,the redis server and client are required to open, and the redis default port is 6379
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
        print("connected success.")
    except:
        print("could not connect to redis.")
    return redis.Redis(connection_pool=pool)
    # return r.lpop('baike_seeds')
if __name__ == '__main__':
    # # info = sys.argv[1]
    # from haxitag.spiders import *
    inf = parse_redis()
    info = sys.argv[1]
    len_split_info = len(info.split('_'))
    split_info = info.split('_')
    if len_split_info == 3:
        channel = split_info[0]
        db_name = split_info[1]
        jobtype = split_info[2]

        # from haxitag.spiders import
        while True:
            url = inf.lpop('baike_seeds')
            print(url)
            BAIKE(url,db_name, channel+"_"+jobtype)
            print("调用成功")
    # elif len_split_info > 2:
    #     # qingdao_five8app_fang_sell_seeds
    #     city = split_info[0]
    #     channel = split_info[1]
    #     task_type = split_info[2]
    #     type = split_info[3]
    #     jobtype = split_info[4]
    #     Baike()
