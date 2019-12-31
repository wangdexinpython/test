
from urllib.parse import urlparse

url ='http://www.baidu.com/post/719.html'
res =urlparse(url)
print (res.netloc)

urlparse(url).netloc