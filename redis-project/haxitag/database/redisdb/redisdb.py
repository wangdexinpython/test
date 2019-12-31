# -*- coding: utf-8 -*-s

import redis
class RdiseDB():
    def __init__():
        # host is the redis host,the redis server and client are required to open, and the redis default port is 6379
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
        print("connected success.")
    
        r = redis.Redis(connection_pool=pool)


