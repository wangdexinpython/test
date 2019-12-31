
from urllib.parse import urlparse

url='m.toutiao.com'

site_name = urlparse(url=url).netloc
print(site_name)