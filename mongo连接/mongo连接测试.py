import urllib.parse,pymongo

client = pymongo.MongoClient("mongodb://xhql:" + urllib.parse.quote_plus(
        "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")["webpage"]["Apps"]

sss = client.find().count()
print(sss)

num=client.find({'id':{"$gt":'100'}}).count()
print(num)

# # [product_mongo]
# dbms = 'mongo'
# host1 = '192.168.1.186'
# port1 = 17018
# host2 = '192.168.1.132'
# port2 = 17018
# host3 = '192.168.1.111'
# port3 = 17018
# user =  'yueli_arabic'
# password = 'sMkjV7!TWsyaHY!14N8U&R7aQ22Ta895'
# database = 'arabic_search'
# charset = 'utf8'
#
# conn = pymongo.MongoClient(
#     "mongodb://{user}:{password}@{host1}:{port1},{host2}:{port2},{host3}:{port3}/{database}".format(
#         user=user,
#         password=urllib.parse.quote_plus(
#             password),
#         host1=host1,
#         port1=port1,
#         host2=host2,
#         port2=port2,
#         host3=host3,
#         port3=port3,
#         database=database))
#
# num = conn.arabic_search.article.find().count()
# print(num)


