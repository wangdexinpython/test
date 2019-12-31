# -*- coding: utf-8 -*-
# @Time : 2019/12/16 16:55
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : 中文符号.py
# @Project : test
'''
pp
'''
import re,hashlib
import zhon.hanzi
from zhon.hanzi import punctuation
# zhon.hanzi
# punctuation = (punctuation+" "+"|")
print("punc",punctuation)
line = '北极光创投 · 邓锋：跨界最大的机会在于%IT和传统行业的融合'
title_hash=""
res = re.sub(u"[%s]+" %(punctuation+" "+"|"+"%"), "", line)

print("res",res)

'''字符串MD5加密'''


def md5_(str):
    md5 = hashlib.md5()
    data = str
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()
s1=""
re1 = md5_(s1)
print("re1",re1)



