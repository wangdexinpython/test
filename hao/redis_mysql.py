# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from db_config import dmpMysqlConfig,dmpRedisConfig,bendiRedisConfig
from mysqldb import MysqlDB
from redisdb import RedisDB
# import join
import json
import time
import binascii
import  joblib


environment = 'dev'
# environment = 'prod'

redis_config = dmpRedisConfig(environment)
redis_config['db'] = 7
redis_conn = RedisDB(config=redis_config).getRedisConn()

mysqlConfig = dmpMysqlConfig(environment)
mysqlConfig['db'] = 'dmp_spider'
mysql_conn = MysqlDB(config=mysqlConfig).getClient()
cur = mysql_conn.cursor()


def get_data():
    """58data"""
    try:
        count = 0
        url_list  = []
        sql = "select source_url from house_five8_spider where house_city=''"
        cur.execute(sql)
        data_list = cur.fetchall()
        print(data_list)
        if data_list:
            for data in data_list:
                for da in data:
                    count+=  1
                    print("da_count:{}".format(count))
                    url_list.append(da)
            return url_list
    except Exception as e:
        print("出错：%s" % str(e))
        mysql_conn.close()


def save_url(seed_list):
    """保存城市为空的url"""
    try:
        count=  0
        with open("/Users/liyang/Documents/zhuge/seed_url581",'w') as f:
            for url in seed_list:
                f.write(str(url)+'\n')
                count+=1
                print("写入条数{}".format(count))
    except Exception as e:
        print("保存数据错误{}".format(str(e)))



# {"spider_config": {"city": "hotcity", "job_type": "details", "task_type": "broker2", "type": "sell", "channel": "five8pc"}, "formdata": {}, "data": {"source_url": "https://wx.58.com/ershoufang/35578234228041x.shtml", "thumbnail": "https://img.58cdn.com.cn/ui9/house/list/lazy_pic.png", "url_crc": ""}, "cookies": {}, "source_url": "https://wx.58.com/ershoufang/35578234228041x.shtml"}




def get_seed():
    """将seed的source_url替换"""
    count = 0
    redis_key = 'broker3_seed'
    with open("/Users/liyang/Documents/zhuge/seed_url581",'r') as f:
        for line in f:
            line = line.rsplit()
            line = ''.join(line)
            # print("line:{}".format(line))
            data_seeds  = {"spider_config": {"city": "hotcity", "job_type": "details", "task_type": "broker3", "type": "sell", "channel": "five8pc"}, "formdata": {}, "data": {"source_url": "https://wx.58.com/ershoufang/35578234228041x.shtml", "thumbnail": "https://img.58cdn.com.cn/ui9/house/list/lazy_pic.png", "url_crc": ""}, "cookies": {}, "source_url": "https://wx.58.com/ershoufang/35578234228041x.shtml"}
            data_seeds["data"]["source_url"] = line
            data_seeds["source_url"]= line
            # print(data_seeds)
            count += 1
            print("导入数据:count{}".format(count))
            try:
                redis_conn.lpush(redis_key,json.dumps(data_seeds))
            except Exception as e:
                print("错误{}".format(str(e)))
                return "+++++++++关闭+++++++++++"


def redis_data():
    """获取redis broker3_seed2"""
    redis_key2  = 'broker3_seed2'
    # for seed2 in redis_conn.lpush(redis_key2):
    try:
        for seed2 in redis_conn.lrange(redis_key2,0,0):
            # seed = json.dumps(seed2)
            seed = seed2.decode('gbk')
            print(seed)
    except Exception as e:
        print("获取失败错误:{}".format(str(e)))


if __name__ == '__main__':

     # url_list = get_data()
     # save_url(url_list)
     # seed_list =get_data()
     # save_url(seed_list)
     get_seed()
