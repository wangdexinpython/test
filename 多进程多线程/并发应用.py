# -*- coding: utf-8 -*-
# @Time : 2019/12/10 16:16
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : 并发应用.py
# @Project : test
'''

'''


# -*- coding:utf-8 -*-
# @Date    : 2019-11-08 19:04:44
# @Author  : wangdexin (wangdexin@haxitag.com)
# @Version : $v1.0.0$
"""
API 搜藏app的订阅查询接口
1.php发送标签，提供引擎数据召回功能。
"""
from flask import Flask,request
from sanic import Sanic
import requests,platform,json,threading,random,operator,asyncio
now_node = platform.node()
if now_node=="WINDOWS-GI073J5":
    hosts = "39.98.232.174"
else:
    hosts="172.26.26.133"
app = Flask(__name__)
@app.route('/api',methods=['POST','GET'])
def Api():
    url = 'http://'+hosts+':8360/jsearch.htm?&dbglv=1&rewrite=1&dbg=2&cache=0&count=20&maxrrec=1200&maxview=512&nouniq=1&start={}&param=sep_uniq:1|sep_fuzzy:0|sep_dint:1&kw= label:{} tags:recommend'
    if request.method=='POST':
        data = request.form
        label_list = data.get('label','').split(' ')
        page_num=data.get("page","1")
        user_id=data.get("user_id","")
        li1=[]
        len_label=len(label_list)
        if len_label<=6:
            print(label_list)
            loop = asyncio.get_event_loop()
            to_do = [get_engine(words) for words in label_list]
            wait_coro = asyncio.wait(to_do)
            res = loop.run_until_complete(wait_coro)
            loop.close()
            print(res)
        #     for i in label_list:
        #         url_parms = url.format((int(page_num)-1)*10,i)
        #         data = get_engine(url_parms)
        #         cons_li = data.get("result","")
        #         count = data.get("count","")
        #         if count>(int(page_num)-1)*10:
        #             li1.extend(cons_li)
        #     li_cons=list_remove(li1)
        #     return json.dumps(li_cons,ensure_ascii=False)
        # else:
        #     label_index = random.sample(range(1,len_label), 6)
        #     for i in label_index:
        #         url_parms = url.format((int(page_num) - 1) * 10, label_list[i])
        #         data = get_engine(url_parms)
        #         cons_li = data.get("result", "")
        #         count = data.get("count", "")
        #         if count > (int(page_num) - 1) * 10:
        #             li1.extend(cons_li)
        #     li_cons = list_remove(li1)
        #     return json.dumps(li_cons, ensure_ascii=False)




def list_remove(li):
    li_=[]
    for i in li:
        if i not in li_:
            li_.append(i)
    reverse_li=sorted(li_,key=operator.itemgetter("crawl_time"),reverse=True)
    return reverse_li
async def get_engine(url):
    cons = requests.get(url).text
    # cons = con.replace("<\/b>","").replace("<b>","")
    result = json.loads(cons).get("result","")
    count=json.loads(cons).get("count","")
    return {"result":result,"count":count}
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8212)





