# # -*- coding: utf-8 -*-
# # scp -r mongo_test.py tanliqiu@search:/home/tanliqiu/search/ytt/search1/raw_data/src_data/
# import pymongo,urllib.parse,os,pexpect,json,re,time
# from urllib.parse import urlparse
#
# dbms = 'mongo'
# host1 = '192.168.1.186'
# port1 = 17018
# host2 = '192.168.1.132'
# port2 = 17018
# host3 = '192.168.1.111'
# port3 = 17018
# user =  'yueli_arabic'
# password = 'sMkjV7!TWsyaHY!14N8U&R7aQ22Ta895'
# database = 'arabic_search'
# charset = 'utf8'
# class Arabic(object):
#     def __init__():
#         conn = pymongo.MongoClient(
#             "mongodb://{user}:{password}@{host1}:{port1},{host2}:{port2},{host3}:{port3}/{database}".format(user=user,password=urllib.parse.quote_plus(password),
#                 host1=host1,
#                 port1=port1,
#                 host2=host2,
#                 port2=port2,
#                 host3=host3,
#                 port3=port3,
#                 database=database))
#         filetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
#         filename = 'inc_arabic_{}.dat'.format(filetime)
#
#     def parse():
#         num=conn.arabic_search.article.find({"nlp_state":1,"state_engine":{'$exists': False}}).count()
#         print("num",num)
#         if num>0:
#             f = open(r'/home/wangdexin/Datapipeline/{}'.format(filename), 'a', encoding='utf-8')
#             zds = conn.arabic_search.article.find({"nlp_state": 1, "state_engine": {'$exists': False}})
#             for k in zds:
#                 engine_dict = engine_data(k)
#                 content = engine_dict.get("content","")
#                 if content!="":
#                     f.write('{}\n'.format(json.dumps(engine_dict, ensure_ascii=False)))
#                 s1 = {'article_id': engine_dict['id']}
#                 s2 = {'$set': {"state_engine": 1}}
#                 conn.arabic_search.article.update(s1,s2)
#             f.close()
#             copy_data_to_engine()
#     def engine_data(,data):
#         engine_dict = {}
#         engine_dict['id'] = str(data.get('article_id', ''))
#         engine_dict['link'] = str(data.get('article_id', ''))
#         engine_dict['title'] = str(data.get('title', ''))
#         engine_dict['content'] = re.sub(r"<[^>]*>","",str(data.get('content', '')))
#         engine_dict['article_url'] = str(data.get('url', ''))
#         engine_dict['author'] = str(data.get("author", ""))
#         engine_dict['site_name'] = str(data.get("site_name",""))
#         engine_dict['flag'] = '0'
#         engine_dict['crawl_time'] = str(data.get('time_stamp', ''))
#         data_label_entity = find_label_entity(data.get('bilstm_label',{}),data.get("bilstm_entity",{}),data.get("bilstm_category",""))
#         engine_dict['label'] = data_label_entity[0]
#         engine_dict['topic'] = data_label_entity[1]
#         engine_dict['type'] = data_label_entity[2]
#         engine_dict['source'] = str(data.get("source", ""))
#         engine_dict['data_type'] = 'arabic'
#         engine_dict['db_table'] = 'article'
#         engine_dict['tags'] = 'recommend'
#         engine_dict['recommend'] = '1'
#         return engine_dict
#     def find_label_entity(,label,entity,category):
#         label=dict_str(label)
#         entity=dict_str(entity)
#         category=dict_str(category)
#         return [label,entity,category]
#     def dict_str(,di):
#         li=[]
#         for k in di:
#             li.append(k.get("tag",""))
#         return ' '.join(li)
#     def copy_data_to_engine():
#         file2 = '/home/wangdexin/Datapipeline/{}'.format(filename)
#         if os.path.getsize('{}'.format(file2)):
#             cmd = "scp -r {} tanliqiu@search:/home/tanliqiu/search/ytt/search1/raw_data/src_data/".format(file2)
#             pexpect.run(cmd)
#         else:
#             pass
#
# if __name__ == '__main__':
#     arabic=Arabic()
#     arabic.parse()
