# -*- coding: UTF-8 -*-
from pymongo import MongoClient
import urllib.parse


class FenLei(object):
    def __init__():
        client = MongoClient("mongodb://xhql:" + urllib.parse.quote_plus(
            "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@47.92.174.37:20388/webpage")
        mydb = client['webpage']
        mycol = mydb["medical_qa"]

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }

    def parse(, skip):
        data_list = mycol.find().limit(1000).skip(skip)
        # print()
        # while True:
        for k in data_list:
            try:
                text = k.get('problem','')
                print('--------------------------------------------------- ' + str(skip))
                print('| ' + text)
                print('| 请选择分类：1:问答  2:疾病  3:症状  4:经验  5:权威信息 6:跳过')
                num = input()
                save_text(num, text)

                skip += 1
            except:
                break

    def save_text(, num, text):
        file_name = ''
        if num == '1':
            file_name = '问答'
        elif num == '2':
            file_name = '疾病'
        elif num == '3':
            file_name = '症状'
        elif num == '4':
            file_name = '经验'
        elif num == '5':
            file_name = '权威信息'
        elif num == '6':
            return
        else:
            print('输入错误，请重新输入')
            num = input()
            save_text(num, text)

        with open(file_name + '.txt', 'a', encoding='utf-8') as f1:
            f1.write(text + '\n')
        # print('|')
        print('| ' + file_name + '  ' + text)
        # print()


if __name__ == '__main__':
    fenlei = FenLei()

    # 参数请自定义数字
    fenlei.parse(2390)
