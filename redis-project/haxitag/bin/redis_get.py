# -*- coding: utf-8 -*-
import sys,os,time
# reload(sys)
# sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(__file__)+"/../../")
sys.path.append("../../")
from haxitag.database.redisdb.redisdb import RedisDB


r = RedisDB().r

rr = r.get('baike_seeds')

print(rr)











