import pymongo,time
from datetime import  datetime
# import datetime
# print(datetime)
s1 = 'test'
s2='date_test'
date_year=time.strftime("%Y")
date_month=time.strftime("%m")
print(date_month)
date_day=time.strftime("%d")
# print(type(date_1))
client = pymongo.MongoClient("127.0.0.1:27017")[s1][s2]
# count = client.find({"mark_time":datetime(2019,6,19)})
# 查询今天的
# count = client.find({"mark_time" : {"$gte": datetime(int(date_year), int(date_month), int(date_day))}})
# 查询昨天的
count=client.find({"mark_time" : {"$gte": datetime(int(date_year), int(date_month), int(date_day)-1),"$lte": datetime(int(date_year), int(date_month), int(date_day))}})
print(count)
for i in count:
    print(i['mark_time'])



# for k in count1:
#     print('1',k['mark_time'])
# "crawler.date" : {"$gte": datetime(2018, 11, 14)}