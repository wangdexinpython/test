import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import re,requests
from lxml import etree
from scrapy.selector import Selector
path = r'C:\Users\EDZ\Documents\WeChat Files\wodexinwolai\FileStorage\File\2019-05/chromedriver'
driver = webdriver.Chrome(executable_path=path)
# driver = webdriver.Firefox()
# wait = WebDriverWait(driver,10)

def search():
    try:
        driver.get('https://www.google.com/search?biw=1536&bih=890&ei=ZomJXceaOtCbmAWyi7egCg&q=competition+definition&oq=commp&gs_l=psy-ab.3.1.0i67l3j0i10l7.8182.9766..12758...0.0..0.135.565.0j5......0....1..gws-wiz.......0.KfvdJE90Egw')
        response = driver.page_source
        time.sleep(10)
        html = etree.HTML(response)
        title = html.xpath('//div[@class="match-mod-horizontal-padding hide-focus-ring cbphWd"]/text()')
        content = Selector(text=response).xpath('//span[@class="ILfuVd NA6bn"]').extract()
        for titles,contents in zip(title,content):
            con = Selector(text=contents).xpath('//text()').extract()
            con = ''.join(con)
            print(titles,con)
    except TimeoutException:
        return search()


if __name__ == '__main__':
    # sea = input('请输入：')
    total = search()