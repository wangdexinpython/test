import json
import requests,random,time,threading,redis

try:
    # host is the redis host,the redis server and client are required to open, and the redis default port is 6379
    pool = redis.ConnectionPool(host='172.26.26.132', port=8991, db=1,password='28JCi*289V92ofj2owoBkv8282928SKVISmv8920565LjhMcs')
    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=9)
    r = redis.Redis(connection_pool=pool)
    print("connected success.")
except:
    print("could not connect to redis.")
def ip_host():
    while True:
        print("00000")
        time.sleep(2)
        proxy = requests.get(
            url="http://d.jghttp.golangapi.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=").text
        pro = json.loads(proxy)
        print(pro)
        if pro['data'] != []:
            proxy_ip = (pro['data'][0]["ip"])
            proxy_port = (pro['data'][0]["port"])
            ip_port = proxy_ip + ":" + proxy_port
            proxy = {
                'https': ip_port
            }
            print("9999")
            long_ = r.llen("ip_test")
            print(long_)
            print("任务进行")
            if long_ <10:
                r.lpush('ip_test', str(proxy))
            else:
                r.rpop('ip_test')
                r.lpush('ip_test', str(proxy))
if __name__ == '__main__':
    ip_host()