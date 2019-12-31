# -*- coding: utf-8 -*-
# @Time : 2019/12/3 19:29
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : scp_engine.py
# @Project : test
'''
入引擎脚本
'''
import os,pexpect

def copy_data_to_engine():
    cmd1="ls /home/wangdexin/Datapipeline/"
    result = pexpect.run(cmd1)
    print(result)
    file2 = '/home/wangdexin/Datapipeline/{}'.format('s')
    if os.path.getsize('{}'.format(file2)):
        cmd = "scp -r {} tanliqiu@search:/home/tanliqiu/search/ytt/search1/raw_data/src_data/".format(file2)
        pexpect.run(cmd)
    else:
        pass
copy_data_to_engine()









