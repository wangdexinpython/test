import pymongo,urllib
from urllib import parse
from pymongo import MongoClient
from bson.objectid import ObjectId
def mongodb():
    mongo = pymongo.MongoClient(
        "mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"172.26.26.132@:20388/dailypops")['dailypops']
    return mongo
mon = mongodb()
db = mon.dailypops
my_set = db.dailypops
my_set.insert({'name':'wang'})
# my_set.save()


# print(ss)