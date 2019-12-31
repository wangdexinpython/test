

import requests,json
url = "https://blog.csdn.net/qq_41676216/article/details/80671381"
html = requests.get(url)
con = html.headers
data = json.loads(json.dumps(dict(con)))
print(data['Date'])
print(type(data))
# con = html.headers["data"]
# print(con)
