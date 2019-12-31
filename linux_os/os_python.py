# -*- coding: utf-8 -*-
# @Time : 2019/12/23 10:38
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : os_python.py
# @Project : test
'''
服务器上liunx和python交互
'''
import os,pexpect
cmd="ps aux|grep mongo"
res = pexpect.run(cmd)
print(res)





