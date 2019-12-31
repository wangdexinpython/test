# -*- coding: utf-8 -*-
# coding: utf-8
import re,json,time,random,linecache
import chardet
def read_txt():
    with open('./人名.txt','r',encoding='utf8') as f:
        count = len(f.readlines())
        # count = len(open('hello.txt', 'rU').readlines())  # 获取行数
        hellonum = random.randrange(1, count, 1)  # 生成随机行数
        ss = linecache.getline('./人名.txt', hellonum)  # 随机读取某行
        return ss.replace('\n','')
def read_name():
    with open('./honour.txt','r',encoding='utf-8') as f1:
        zds = f1.readlines()
        for i in zds:
            ss = read_txt()
            da = i.replace('吴恩达',ss)
            print(da)
            write_name(da)
def write_name(da):
    with open('./honour_1.txt','a+',encoding='utf-8') as f2:
        f2.write(da)
read_name()