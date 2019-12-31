from scrapy.crawler import CrawlerProcess
from crawlProcess.baike.BAI import BaikeSpider
from scrapy.utils.project import get_project_settings
process = CrawlerProcess()
process.crawl(BaikeSpider)
process.start()


# 多进程和scrapy的twited冲突错误。
list=['baike','zhihu','toutiao']
for pro in list:
    process.crawl(pro)
process.start()












