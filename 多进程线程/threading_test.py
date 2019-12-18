# import threading,time
# def do_something(da):
#     time.sleep(10)
#     print(da)
# while True:
#     for j in range(0,5):
#         arg = threading.Thread(target=do_something,args=(j,))
#         arg.setDaemon(True)
#         arg.start()
#     for k in range(22,27):
#         arg = threading.Thread(target=do_something, args=(k,))
#         arg.setDaemon(True)
#         arg.start()
#     arg.join()
#     print("end")


# def




# -*- coding:utf-8 -*-
import sys
sys.path.append("../../")
sys.path.append("/mnt/home/wangdexin/datapipeline/")
import pymongo,time,requests,json,os,urllib.parse,re,copy,threading
from urllib.parse import urlparse
from database.mongodb import MongoDB
import urllib.parse
import redis,pexpect
environment='server'
db_name_web='webpage'
# db_name_topic='topic'
class APPS(object):
    def __init__(self):
        self.mog_content = MongoDB(environment=environment, db_name=db_name_web).client
    def parse(self):
        while True:
            zds = self.mog_content.webpage.baike_engine.find({'state':0}).limit(10000)
            print("begin")
            li_group = self.get_find_all_data_list(zds)
            # self.thread_content(li_group)
            li_group_all = self.merge_partition_list(li_group, 10)
            for m in li_group_all[0:6]:
                t = threading.Thread(target=self.thread_content, args=(m,))
                t.setDaemon(True)
                t.start()
            for k in li_group_all[6:10]:
                t = threading.Thread(target=self.thread_content_server, args=(k,))
                t.setDaemon(True)
                t.start()
            t.join()
    def thread_content_server(self,data):
        for m in data:
            content = m.get("content","")
            blistm = m.get("bilstm_entity","")
            if blistm=="":
                label = self.nlp_get_8997_server(content)
                data = self.label_entity(label)
                print('data', "server",data)
                s1 = {'id': m['id']}
                s2 = {'$set': {'bilstm_label': data.get("bilstm_label", ""),
                               "bilstm_entity": data.get("bilstm_entity", ""), 'state': 1}}
                self.mog_content.webpage.baike_engine.update(s1, s2)
            else:
                s1 = {'id': m['id']}
                s2 = {'$set': {'state': 1}}
                self.mog_content.webpage.baike_engine.update(s1, s2)
    def thread_content(self,data):
        for m in data:
            content = m.get("content","")
            blistm = m.get("bilstm_entity","")
            if blistm=="":
                label = self.nlp_get_8997_text(content)
                data = self.label_entity(label)
                print('data', "text",data)
                s1 = {'id': m['id']}
                s2 = {'$set': {'bilstm_label': data.get("bilstm_label", ""),
                               "bilstm_entity": data.get("bilstm_entity", ""), 'state': 1}}
                self.mog_content.webpage.baike_engine.update(s1, s2)
            else:
                s1 = {'id': m['id']}
                s2 = {'$set': {'state': 1}}
                self.mog_content.webpage.baike_engine.update(s1, s2)

    def label_entity(self,data):
        bilstm_data=data
        bilstm_label = ' '.join(json.loads(bilstm_data).get("label", {}).get("content", ""))
        bilstm_entity = json.loads(bilstm_data).get("entity", {}).get("content", "").replace(",", " ")
        data={"bilstm_label":bilstm_label,"bilstm_entity":bilstm_entity}
        return data

    def nlp_get_8997_text(self,data):
        data1 = {"text": data}
        url1 = 'http://172.26.26.135:8997/nlp'
        try:
            cons1 = requests.post(url1, data=data1).text
            return cons1
        except:
            return json.dumps({})
    def nlp_get_8997_server(self,data):
        data1 = {"text": data}
        url1 = 'http://172.26.26.139:8997/nlp'
        try:
            cons1 = requests.post(url1, data=data1).text
            return cons1
        except:
            return json.dumps({})
    def get_find_all_data_list(self,data_list):
        data = []
        while True:
            a = {}
            try:
                text = data_list.next()
                for k, v in text.items():
                    a.update({k: v})
            except:
                break
            data.append(a)
        return data

    # 接收一个列表和数量，将列表拆分为对应数量的子列表
    def merge_partition_list(self, list, num):
        list_len = len(list)
        child_list_len = int(list_len / num) + 1
        copy_list = copy.deepcopy(list)
        parents_list = []
        child_list = []
        for i in list:
            child_list.append(i)
            if len(child_list) == child_list_len:
                parents_list.append(child_list)
                for j in child_list:
                    copy_list.remove(j)
                child_list = []
        if copy_list != []:
            parents_list.append(copy_list)
        # print(parents_list)
        return parents_list
if __name__ == '__main__':
    apps=APPS()
    apps.parse()












