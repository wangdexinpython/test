# -*- coding: utf-8 -*-
# @Time : 2019/12/12 18:28
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : 时间戳to日期.py
# @Project : test

import time
tim = 1576143426409/1000

print(tim)
print(int(tim))
timeStamp = int(tim)
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)






