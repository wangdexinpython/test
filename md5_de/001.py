
# import hashlib
#
# tt = hashlib.md5(1)
# print(tt)
# print(hash(1))
# print(hash(3))
import hashlib

md5 = hashlib.md5()  # 应用MD5算法
data = "m.toutiao.com"
md5.update(data.encode('utf-8'))
print(data)
print(md5.hexdigest())