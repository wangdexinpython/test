
# import re
#
# ss = 'https://baike.baidu.com/item/劳动?force=1"'
#
# s = re.findall('(/item/.*?)[?!force=1]*"',ss)
# # s = re.findall('(/item/.*?)"',ss)
# print(s)

import time,datetime
#
# ss = int(time.time())
#
# date = datetime.


# def now_to_timestamp(digits = 10):
#     time_stamp = time.time()
#     digits = 10 ** (digits -10)
#     time_stamp = int(round(time_stamp*digits))
#     return time_stamp
#
# ss=now_to_timestamp(13)
# print(ss)

crawl_time = datetime.datetime.now().strftime('%Y/%m/%d')
print(crawl_time)


