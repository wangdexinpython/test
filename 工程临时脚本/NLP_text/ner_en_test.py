# -*- coding: utf-8 -*-
# @Time : 2019/12/4 15:39
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : ner_en_test.py.py
# @Project : test
'''
pp
'''

import requests,json
data='''And of the 166 miles of border barrier the U.S. government is planning to build in Texas, new construction has been completed along just 2 percent of that stretch a year before the target completion date, according to the construction data. Just four miles of the planned border wall in Texas is on federal land — the other 162 lie on private property.
Faced with intense pressure to meet Trump’s 500-mile campaign pledge, administration officials have instead prioritized the lowest-hanging fruit of the barrier project, accelerating construction along hundreds of miles of flat desert terrain under federal control in Western states where the giant steel structure can be erected with relative ease'''
def ner_ner_8207(data):
    data1 = {"content": data}
    url1 = 'http://lets.abuzahbi.com/ner'
    try:
        cons1 = requests.post(url1, data=data1).text
        return json.loads(cons1,encoding='utf-8')
    except Exception as e:
        print(e)
        return json.dumps({})

m1 = ner_ner_8207(data)
print(m1)


