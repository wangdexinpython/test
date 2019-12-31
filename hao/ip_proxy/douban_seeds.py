
import requests,hashlib,redis,time
from lxml import etree

class Douban(object):
    def __init__():
        r = parse_redis()
        r2 = parse_redis2()

        ip_list = r2.hkeys('useful_proxy')
        print(ip_list)
        # for i in ip_list:
        proxyMeta = str(ip_list[6], encoding="utf-8")
        # print(sss)
    # proxyMeta = ''
        proxies = {

            "https": "112.66.84.130:8060",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        }
        url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
        url2 = 'https://book.douban.com{}'
        url3 = 'https://book.douban.com{}?start={}&type=T'
    # https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=980&type=T
    def parse():
        cons = requests.get(url,headers=headers,proxies=proxies).content
        selector = etree.HTML(cons)
        cons = selector.xpath("//table[@class='tagCol']/tbody//a/@href")
        print(cons)
        for i in cons:
            for j in range(0,1000,20):
                url = url3.format(i,j)
                print(url)
                time.sleep(0.2)
                try:
                    print("请求开始")
                    con_id = requests.get(url,headers=headers,proxies=proxies).content
                    selec = etree.HTML(con_id)
                    url_id = selec.xpath("//ul[@class='subject-list']//h2/a/@href")
                    print(url_id)
                    for k in url_id:
                        print(k)
                        url_md5 = md5_(k)
                        sta = hash_exist(url_md5)
                        if sta==False:
                            print("入库url",url)
                            hash_(url_md5)
                            r.lpush('douban_seeds',k)
                        else:
                            print('指纹重复')
                except:
                    print('代理出错')
                    r.lpush('douban_seeds_error',url)
    def md5_(, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()

    def parse_redis():
        # pool = redis.ConnectionPool(host='172.26.26.132', port=8991, db=2,password='28JCi*289V92ofj2owoBkv8282928SKVISmv8920565LjhMcs')
        # r = redis.Redis(connection_pool=pool)
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)

        print("redis connected success.")
        return redis.Redis(connection_pool=pool)

    def parse_redis2():
        # pool = redis.ConnectionPool(host='172.26.26.132', port=8991, db=2,password='28JCi*289V92ofj2owoBkv8282928SKVISmv8920565LjhMcs')
        # r = redis.Redis(connection_pool=pool)
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

        print("redis connected success.")
        return redis.Redis(connection_pool=pool)
    def hash_(, str):
        r.hset(name="douban_fingerprint", key=str, value=1)

    def hash_exist(, str):
        return r.hexists(name='douban_fingerprint', key=str)


    def run():
        parse()

if __name__ == '__main__':
    douban = Douban()
    douban.run()