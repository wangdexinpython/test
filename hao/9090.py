

import pymongo
# import pandas as pd

# 连接数据库
client = pymongo.MongoClient(host="10.65.135.51", port=27017)['Spider_Project']['Web_all']

# 读取数据
# data = pd.DataFrame(list(client.find()))
data2 = client.find_one()
# 选择需要显示的字段
data1 = data2['title']
# data2 = data['content']
# 打印输出
print(data1)