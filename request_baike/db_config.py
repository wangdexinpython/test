# -*- coding: utf-8 -*-

import redis
try:
    #host is the redis host,the redis server and client are required to open, and the redis default port is 6379
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
    print("connected success.")
except:
    print("could not connect to redis.")
r = redis.Redis(connection_pool=pool)


list = '300033,600066'
# r.set('stock_codes', list)
