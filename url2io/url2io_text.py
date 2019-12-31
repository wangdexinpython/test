
import requests,re,time
api_='http://url2api.applinzi.com/article?token=B2Iv2c4HQPmUEWjSmdMXzQ&field=text&url='
bas_url=' https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9935691963444919737%22%7D&n_type=0&p_from=1'
url = api_+bas_url
cons = requests.get(url).text

# title=etree.HTML(requests.get(url).text).xpath("//h1[@class='art_tit_h1']/text()")
# title=''.join(title)
print(cons)
from lxml import etree
# url='https://baike.baidu.com/item/钟乳石'
# cont=etree.HTML(requests.get(url).text).xpath("//section[@class='art_pic_card art_content']//p//text()")
# artical=','.join(cont)
# print(artical)


# //article[@class='clearfix']//p/text()


# url2='http://www.jingwohui.com/archives/26167'
# con=etree.HTML(requests.get(url2).text).xpath("//article[@class='clearfix']//p[contains(text(),'参考资料')]/preceding-sibling::p//text()")
# artical1=','.join(con)
# print(artical1)

