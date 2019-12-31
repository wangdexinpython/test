# -*- coding: utf-8 -*-
# @Time : 2019/12/16 10:59
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : simhash_1.py
# @Project : test
'''
pp
'''
# assuming that you have a dictionary with document id as the key and the document as the value:
# documents = { doc_id: doc } you can do:
# from simhash_test import Simhash
import simhash
# documents={"doc_1":"采取第一种方法，若是只比较两篇文章的相似性还好，但如果是海量数据呢","doc_2":"采取第一种方法，若是只比较两篇文章的相似性还好，但如果是海"}
# # from simhash_test import
# def split_hash(str, num):
#     return [ str[start:start+num] for start in range(0, len(str), num) ]
#
# hashes = {}
# for doc_id, doc in documents.items():
#     hash =(doc)
#
#     # you can either use the whole hash for higher precision or split into chunks for higher recall
#     hash_chunks = split_hash(hash, 4)
#
#     for chunk in hash_chunks:
#         if chunk not in hashes:
#             hashes[chunk] = []
#         hashes[chunk].append(doc_id)
#
# # now you can print the duplicate documents:
# for hash, doc_list in hashes:
#     if doc_list > 1:
#         print("Duplicates documents: ", doc_list)

import re
from simhash import Simhash
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    print('s',s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

print('%x' % Simhash(get_features('国网公司系统多位人士以及电力新能源行业专家接受上证报记者采访时表示，大规模电网投资时代正在过去，以泛在电力物联网为标志的电网信息化建设时代已经来临。')).value)
print('%x' % Simhash(get_features('国网公司系统多位人士以及电力新能源行业专家接受上证报记者采访时表示，大规模电网投资时代正在过去。以泛在电力物联网为标志的电网信息化建设时代已经来临。')).value)
print('%x' % Simhash(get_features('How r you?I    am fine. Thanks.')).value)












