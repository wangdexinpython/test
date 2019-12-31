
import requests,re
from lxml import etree
from bs4 import BeautifulSoup
url = 'https://mp.weixin.qq.com/s/54QdwJeXt4NF-j1NzQOJ5w'
def _extract_weixin(url):
    # log.info("parse weixin %s" % (url))
    data = requests.get(url).text
    if '</code>' in data:
        res = re.compile('<code>.*?</code>', re.S).sub('', data)
        html = etree.HTML(res)
        div = html.xpath('//div[@id="js_content"]//p//text()')
        content_n = ''.join(div)
        artical = str(content_n).replace(' ', '').replace('&amp;', '').replace('amp;', '').replace('amp;gt;',
                                                                                                   '').replace('\n',
                                                                                                               '').replace(
            '\r', '').replace('\t', '')
    else:
        html = etree.HTML(data)
        div = html.xpath('//div[@id="js_content"]//p//text()')
        content_n = ''.join(div)
        artical = str(content_n).replace(' ', '').replace('&amp;', '').replace('amp;', '').replace('amp;gt;',
                                                                                                   '').replace('\n',
                                                                                                               '').replace(
            '\r', '').replace('\t', '')
    if not artical:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        con = soup.find('div', class_='rich_media_content').find_all('p')
        cont = str(con)
        artical = re.sub('<[^>]+>', '', cont).replace('[', '').replace(']', '').replace(' ', '').replace(',,,',
                                                                                                         '。').replace(
            ',,,,', '。').replace(',,', '。')
    # log.info("parse weixin get artical %s" % (artical))
    return artical or ""

s1 = _extract_weixin(url)
print(s1)

