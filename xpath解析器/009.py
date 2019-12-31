# -*- coding: utf-8 -*-
import urllib,requests
from scrapy.selector import Selector
url = 'http://news.cctv.com/2019/05/12/ARTIibCCcZP50p9sFwDgFBGq190512.shtml'
response = requests.get(url)
print('resp',response.text)
title = Selector(response).xpath("//h1/text()").extract()
print('11',title)
title1 = Selector(response).xpath("//h1/text()").extract_first()
print('sss',title1)