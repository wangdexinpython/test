# -*- coding: utf-8 -*-
# @Time : 2019/12/10 14:31
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : python_map.py
# @Project : test
'''
pp
'''

from multiprocessing import Pool
import time
def func(i): #返回值只有进程池才有,父子进程没有返回值
    time.sleep(0.5)
    return i*i

if __name__ == '__main__':
    p = Pool(5)
    ret = p.map(func,range(10))
    print(ret)








