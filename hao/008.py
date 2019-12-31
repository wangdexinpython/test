
# import hashlib
#
# tt = hashlib.md5(1)
# print(tt)
# print(hash(1))
# print(hash(3))
# import hashlib
#
# md5 = hashlib.md5()  # 应用MD5算法
# data = "https://baike.baidu.com/item/%E6%9C%9D%E7%BE%8E%E9%A6%96%E8%84%91%E7%AC%AC%E4%BA%8C%E6%AC%A1%E4%BC%9A%E6%99%A4/23308281"
# md5.update(data.encode('utf-8'))
# print(data)
# print(md5.hexdigest())


# def __init__():
#     # 创建数据库连接
#     client = MongoClient("mongodb://xhql:" + urllib.parse.quote_plus(
#         "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")
#
# def process_item(, item, spider):
#     # 将数据写入数据库
#     client = MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")
#     client.webpage.baike_details.insert(item)
#     return item
import re
string="<script>var uid = '';var BLOG_URL = 'https://blog.51cto.com/';</script>"
# pattern="[a-zA-Z]+://[0-9a-zA-Z./]*[.comn]*"
pattern="[a-zA-Z]+://[^\s]*[(.com)|(.cn)]+"

result=re.search(pattern,string)
print(result.group(0))



