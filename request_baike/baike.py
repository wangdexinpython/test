# -*- coding: utf-8 -*-
import requests
import re
import hashlib
import json
import redis
try:
    #host is the redis host,the redis server and client are required to open, and the redis default port is 6379
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
    print("connected success.")
except:
    print("could not connect to redis.")
r = redis.Redis(connection_pool=pool)
from lxml import etree
class Baike(object):
    def __init__():
        url = 'https://baike.baidu.com/item/%E7%BE%8E%E5%9B%BD/125486?fromtitle=%E7%BE%8E%E5%88%A9%E5%9D%9A%E5%90%88%E4%BC%97%E5%9B%BD&fromid=379269'
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
    def parse(,url):
        html = requests.get(url,headers = headers)
        con = html.content
        con1 = con.decode('utf-8')
        links = re.findall('href="(/item/.*?)"',con1)
        print(len(links))
        list1 = links[5:-1]
        if list1!=[]:
            redis_config(list1)
        else:
            print("页面没有符合要求的词条")
    def redis_config(,li):
        for i in li:
            print(i)
            url = "https://baike.baidu.com"+i
            md5_data = md5_(url)
            sta = hash_exist(md5_data)
            if sta == False:
                print("入库待抓url:%s" %(url))
                hash_(md5_data)
                fo_ce = re.findall('force=',url)
                if fo_ce==[]:
                    r.lpush('baike_seeds', url)
                r.lpush('baike_deep_seeds',url)
    def md5_(,str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()
    def deep_():
        print(r.llen('baike_deep_seeds'))
        print(r.llen('baike_seeds'))
        url = r.lpop('baike_deep_seeds')
        if url != None:
            # ip_ = proxy_ip()
            parse(url)
        else:
            print("数据已经抓取完")
    def hash_(,str):
        return r.hset(name="baike_fingerprint", key=str, value=1)
    def hash_exist(,str):
        print(r.hlen('baike_fingerprint'))
        return r.hexists(name='baike_fingerprint',key=str)
    def run():
        # parse(url)
        while True:
            deep_()
    def proxy_ip():
        proxy = requests.get(
            url="http://d.jghttp.golangapi.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=").text
        pro = json.loads(proxy)
        print(pro)
        if pro['data'] != []:
            proxy_ip = (pro['data'][0]["ip"])
            proxy_port = (pro['data'][0]["port"])
            ip_port = proxy_ip + ":" + proxy_port
            print(ip_port)
            return {
                'https': ip_port
            }
        else:
            return ''

if __name__ == '__main__':
    baike = Baike()
    baike.run()

