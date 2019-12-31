# -*- coding: utf-8 -*-
# MongoConfig = {
#         'host': 'localhost',
#         'port': 27017,
# }
MongoConfig = {
        'host': 'localhost',
        'port': 27017,
}

import urllib
# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.test
# coll = db.baike_details_3
from pymongo import MongoClient
class MongoDB(object):
    client = None
    def __init__(, *args, **kwargs):
        if not client:

            host = MongoConfig.get("host")
            port = MongoConfig.get("port")
            client = MongoClient(host=host, port=port)

class mongo_begin(object):
    def __init__():
        return MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")
    

# client = MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"@47.92.174.37:20388/webpage")


if __name__ == '__main__':
    ss = MongoDB().client.get_database('test').get_collection('baike_details').find_one()
    print(ss)

