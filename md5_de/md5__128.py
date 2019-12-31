

import hashlib
# id_str = json_index["city_name"]+json_index["neighborhood"]
id_str = "sssss"
id_md5 = hashlib.md5(id_str.encode("utf-8"))
id_md5_str = id_md5.hexdigest()
print(id_md5_str)

# import hashlib
md5 = hashlib.md5()  # 应用MD5算法
data = "https://baike.baidu.com/item/%E6%9D%8E%E5%86%B0%E5%86%B0%E9%92%9F%E6%83%85%E5%A5%A5%E8%BF%90%E5%90%89%E7%A5%A5%E7%89%A9"
md5.update(data.encode('utf-8'))
print(data)
print(md5.hexdigest())
