# -*- coding: utf-8 -*-
# @Time : 2019/12/27 17:20
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : ftp_1.py
# @Project : test
'''
ftp客户端,,中文文件名问题会产生拉丁1错误。。需要设置，中文编码，，文本内内容不受影响。
传输数据模式，ASCII，和二进制模式。
传输过程模式，主动模式，被动模式。
'''
# import os
#

from ftplib import FTP
import os
ftp=FTP()
# ftp.makepasv()
ftp.set_debuglevel(2)
ftp.encoding='GB2312'
ftp.connect("47.110.55.112",21)
ftp.login("hyu5708250001","Yueli20190124")
ftp.retrlines('LIST')

# ftp.cwd("htdocs")
# ftp.nlst("/htdocs")

def upload(f, remote_path, local_path):
    fp = open(local_path, "rb")
    # fp = ftp.retrlines(local_path)

    buf_size = 1024
    f.storbinary("STOR {}".format(remote_path), fp, buf_size)
    # f.storlines("STOR {}".format(remote_path),fp,buf_size)
    fp.close()

# dir = os.listdir("./article")
# for file in dir:
#     upload(ftp,"/htdocs/report/".format(file),"./article/{}".format(file))


upload(ftp,"/htdocs/report/我7459eefefeaaf7958da2a5a11097cec4.html","./article/我7459eefefeaaf7958da2a5a11097cec4.html")





















