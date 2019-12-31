# -*- coding: utf-8 -*-
# @Time : 2019/12/18 17:48
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : v2.py
# @Project : test
'''

'''
# from weibo_spider import WeiBo
url="https://card.weibo.com/article/m/show/id/2309404363550268218951?_wb_client_=1&from=groupmessage"
# ww = WeiBo(url).parse()
# print(ww)

from weibos_test import Weibo

res = Weibo(url).parse()
print(res)

