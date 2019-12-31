# -*- coding: utf-8 -*-

from haxitag.databas.config.db_config import db_conifg

MongoConfig = {
        'host': 'localhost',
        'port': 27017,

}

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
coll = db.baike_details_3


from pymongo import MongoClient
class MongoDB(object):
    client = None
    def __init__(, *args, **kwargs):
        if not client:
            host = MongoConfig.get("host")
            port = MongoConfig.get("port")
            client = MongoClient(host=host, port=port)




