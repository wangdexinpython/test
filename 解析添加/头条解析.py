import requests,time,json,re
from lxml import etree
url = 'https://www.toutiao.com/a6726701359229305351'
def _extract_toutiao(url):
    # log.info("parse toutiao %s" % (url))
    url = url.replace("m.toutiaocdn.com", "www.toutiao.com")
    url = url.replace("m.toutiaocdn.cn/group/", "www.toutiao.com/a").replace("www.toutiao.com/item/",
                                                                             "www.toutiao.com/a").replace(
        "www.toutiao.com/group/", "www.toutiao.com/a")
    s = requests.Session()
    # s.mount('http://', HTTPAdapter(max_retries=3))
    # s.mount('https://', HTTPAdapter(max_retries=3))
    response = s.get(url, timeout=5)
    response_text = response.text
    artical_pat = re.compile(u"(?<=content:)[\w\W]*?(?=groupId)")
    articals = artical_pat.findall(response_text) and artical_pat.findall(response_text)[0] or ""
    articals_html = re.sub(r"<[^>]*>",'',articals.encode('utf8').decode("unicode-escape"))
    artical = re.sub(r"&.*?;", "", articals_html).encode('raw_unicode_escape').decode('utf8').replace('.slice(6, -6)','')
    return artical or ""
res = _extract_toutiao(url)
print(res)

# articals_html = re.sub(r"<[^>]*>", '', content)
