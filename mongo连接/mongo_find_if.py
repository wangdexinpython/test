import pymongo,urllib,re
from urllib import parse

def mongodb():
    mongo = pymongo.MongoClient(
        "mongodb://dailypops:" + urllib.parse.quote_plus("1!2@3#aAdD")+"@47.92.174.37:20388/dailypops")['dailypops']
    return mongo
mon = mongodb()
# ss = mon.event.find({'event':re.compile('BR')}).count()
ss=mon.event.find_one({'event_id':'22'})
if ss==None:
    print("1111")
print(ss)



