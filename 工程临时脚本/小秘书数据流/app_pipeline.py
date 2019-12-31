# # -*- coding: utf-8 -*-
# # @Time : 2019/12/5 20:57
# # @Author : EDZ
# # @Email : wangdexin@haxitag.com
# # @File : app_pipeline.py.py
# # @Project : test
# '''
# pp
# '''
#
# # -*- coding:utf-8 -*-
# import sys
#
# sys.path.append("../../")
# sys.path.append("/mnt/home/wangdexin/datapipeline/")
# import time, requests, os, re, operator
# import urllib.parse, json, pexpect
# from urllib.parse import urlparse
# from database.mongodb import MongoDB
# from database.mysqldb import MysqlDB
#
# db_name_contents = 'integrate'
# db_name_topic = 'topic'
# da_name_sql = 'sc'
#
#
# class APP_data(object):
#     def __init__():
#         # find_time = int((time.time())*1000)-300000
#         # filetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
#         filename = 'full_app.dat'
#         # f = open(r'./app_full.dat', 'a', encoding='utf-8')
#         mog_content = MongoDB(db_name=db_name_contents).client
#         mog_topic = MongoDB(db_name=db_name_topic).client
#         mys = MysqlDB(db_name=da_name_sql).getClient()
#         cur = mys.cursor()
#
#     def get_mongo():
#         count = mog_content.integrate.contents.find({}).count()
#         print('count', count)
#         if count > 0:
#             f = open(r'/mnt/data/liqiu/SOUCANF_APP/{}'.format(filename), 'a', encoding='utf-8')
#             webnum = mog_content.integrate.contents.find({})
#             for one in webnum:
#                 data_return = engine_data(one)
#                 # read_data_to_topic(data_return)
#                 f.write('{}\n'.format(json.dumps(data_return, ensure_ascii=False)))
#             f.close()
#             # copy_data_to_engine()
#
#     def engine_data(, data):
#         html_type = data.get("type", "")
#         if html_type == "html":
#             engine_dict = {}
#             len_num = len(str(data.get('content', '')))
#             if len_num > 10:
#                 engine_dict['id'] = str(data.get('_id', ''))
#                 engine_dict['uid'] = str(data.get('uid', ''))
#                 engine_dict['link'] = str(data.get('_id', ''))
#                 engine_dict['title'] = str(data.get('title', ''))
#                 engine_dict['content'] = str(data.get('content', ''))
#                 engine_dict['source'] = 'user'
#                 engine_dict['article_url'] = str(data.get('path', ''))
#                 engine_dict['flag'] = '0'
#                 engine_dict['site_name'] = str(urlparse(data.get('path', '')).netloc)
#                 engine_dict['author'] = ''
#                 engine_dict['crawl_time'] = str(data.get('create_time', ''))[0:10]
#                 engine_dict['doc_groups'] = app_album_ids(data)
#                 engine_dict['label'] = label_mongo(data)
#                 engine_dict['topic'] = entity_mongo(data)
#                 engine_dict['album_id'] = get_album_id(engine_dict.get('uid', ''))
#                 engine_dict['type'] = AI_get_nlp(engine_dict.get('content', ''))
#                 engine_dict['data_type'] = '搜藏'
#                 engine_dict['db_table'] = 'contents'
#                 engine_dict['ispubgroup'] = get_ispubgroup_state(get_ispubgroup_album_id(),
#                                                                       engine_dict['doc_groups'])
#                 engine_dict['recommend'] = '1'
#                 engine_dict['tags'] = 'ispubgroup recommend'
#             return engine_dict
#         else:
#             len_num = len(str(data.get('content', '')))
#             engine_dict = {}
#             if len_num > 10:
#                 engine_dict['id'] = str(data.get('_id', ''))
#                 engine_dict['uid'] = str(data.get('uid', ''))
#                 engine_dict['link'] = str(data.get('_id', ''))
#                 engine_dict['title'] = str(data.get('title', ''))
#                 engine_dict['content'] = str(data.get('content', ''))
#                 engine_dict['source'] = 'user'
#                 engine_dict['article_url'] = str(data.get('path', ''))
#                 engine_dict['flag'] = '0'
#                 engine_dict['site_name'] = str(urlparse(data.get('path', '')).netloc)
#                 engine_dict['author'] = ''
#                 engine_dict['crawl_time'] = str(data.get('create_time', ''))[0:10]
#                 engine_dict['doc_groups'] = app_album_ids(data)
#                 engine_dict['label'] = label_mongo(data)
#                 engine_dict['topic'] = entity_mongo(data)
#                 engine_dict['album_id'] = get_album_id(engine_dict.get('uid', ''))
#                 engine_dict['type'] = AI_get_nlp(engine_dict.get('content', ''))
#                 engine_dict['data_type'] = '搜藏'
#                 engine_dict['db_table'] = 'contents'
#                 engine_dict['ispubgroup'] = get_ispubgroup_state(get_ispubgroup_album_id(),
#                                                                       engine_dict['doc_groups'])
#                 engine_dict['tags'] = 'ispubgroup'
#             return engine_dict
#
#     def get_album_id(, uid):
#         sql = '''select id from album where uid="{}"'''.format(uid)
#         cur.execute(sql)
#         num = cur.fetchall()
#         dd = []
#         for i in num:
#             if i:
#                 dd.append(str(i[0]))
#         return ' '.join(dd)
#         # 适配小组ID不同的函数
#
#     def app_album_ids(, data):
#         try:
#             if "app_album_ids" in data.keys():
#                 doc_groups = str(data.get('app_album_ids', ''))
#             elif "app_album_id" in data.keys():
#                 if isinstance(data.get('app_album_id', ''), list):
#                     # doc_groups=' '.join(data.get('app_album_id', ''))
#                     doc_groups = ' '.join('%s' % id for id in data.get('app_album_id', ''))
#                 else:
#                     doc_groups = str(data.get('app_album_id', ''))
#             else:
#                 doc_groups = ""
#             return doc_groups
#         except:
#             return ""
#         # if data.get('app_album_ids', '') == '' and data.get('app_album_id', '') == '':
#         #     doc_groups = ""
#         # elif data.get('app_album_ids', '') == '' and data.get('app_album_id', '') != '':
#         #     num_id = data.get('app_album_id', '')
#         #     doc_groups = ' '.join('%s' % id for id in num_id) if num_id != "" else ""
#         # elif data.get('app_album_id', '') == '' and data.get('app_album_ids', '') != '':
#         #     doc_groups = str(data.get('app_album_ids', ''))
#         # else:
#         #     doc_groups = ""
#         # return doc_groups
#
#     # 获取公开小组的ID列表，判断数据是否公开
#     def get_ispubgroup_album_id():
#         sql = '''select * from album where `type` =3 and recommend =1'''
#         cur.execute(sql)
#         num = cur.fetchall()
#         dd = []
#         for i in num:
#             dd.append(str(i[0]))
#         return dd
#
#     # 判断本文章是否属于公开组
#     def get_ispubgroup_state(, pub_dd, album_id):
#         stas = 0
#         li_album = album_id.split(' ')
#         for id_s in li_album:
#             if id_s in pub_dd:
#                 stas = 1
#         return str(stas)
#
#     def AI_get_nlp(, data):
#         url = 'http://172.26.26.139:8995/topic?content={}'.format(data)
#         ai = requests.get(url).text
#         type_nlp = 'ai' if ai == 'AI' else ''
#         return type_nlp
#
#     def entity_mongo(, di):
#         edit_bilstm_entity = dict_list(di.get("edit_bilstm_entity", ""))
#         bd = dict_list(di.get('bd_entity', ''))
#         core = dict_list(di.get('core_entity', ''))
#         bilstm = dict_list(di.get('bilstm_entity', ''))
#         li1 = []
#         li1.extend(edit_bilstm_entity)
#         li1.extend(bilstm)
#         li1.extend(core)
#         li1.extend(bd)
#         return len_entity(li1)
#
#     def len_entity(, li1):
#         li_str = ' '.join(special_sign(list(set(li1))))
#         li_res = li_str[0:1024].split(' ')[0:-1]
#         return ' '.join(li_res)
#
#     def label_mongo(, dic):
#         app_tags = []
#         edit_bilstm_entity = dict_list(dic.get("edit_bilstm_entity", ""))
#         app_tags.extend(edit_bilstm_entity)
#         if dic.get('app_tags', '') != '':
#             app_tags.extend(dic.get('app_tags', '').split(','))
#         user_tags = dic.get("user_tags", [])
#         app_tags.extend(user_tags)
#         app_tags.extend(dict_list(dic.get('bilstm_entity', '')))
#         app_tags.extend(dict_list(dic.get('bilstm_label', '')))
#         app_tags.extend(dict_list(dic.get('core_label', '')))
#         app_tags.extend(dict_list(dic.get('core_entity', '')))
#         app_tags.extend(dict_list(dic.get('bd_label', '')))
#         app_tags.extend(dict_list(dic.get('bd_entity', '')))
#         return len_entity(app_tags)
#
#     # 书名号实体标签的处理，
#     def special_sign(, li):
#         label_2 = []
#         for m in li:
#             if "《" in m:
#                 m1 = m.replace("《", "").replace("》", "")
#                 label_2.append(m)
#                 label_2.append(m1)
#             else:
#                 label_2.append(m)
#         list_after = label_2
#         return list_after
#
#     def read_data_to_topic(, data):
#         topic_dict = {}
#         if data.get('type', '') == 'ai':
#             topic_dict['id'] = data.get('id', '')
#             topic_dict['content'] = data.get('content', '')
#             topic_dict['crawl_time'] = data.get('crawl_time', '')
#             topic_dict['site'] = data.get('source', '')
#             topic_dict['source'] = 'soucang'
#             topic_dict['AI_source'] = 'article'
#             topic_dict['topic'] = data.get('type', '')
#             topic_dict['type'] = data.get('topic', '')
#             topic_dict['url'] = data.get('article_url', '')
#             topic_dict['label'] = data.get('label', '')
#             if data.get('title', '') == '':
#                 first_word = re.findall('^(.*?)。', data.get('content', ''))
#                 first_dou = re.findall('^(.*?),', data.get('content', ''))
#                 if first_word != []:
#                     topic_dict['title'] = ''.join(first_word)
#                 elif first_dou != []:
#                     topic_dict['title'] = ''.join(first_dou)
#                 else:
#                     topic_dict['title'] = data.get('content', '')
#             else:
#                 topic_dict['title'] = data.get('title', '')
#             mog_topic.topic.AI_topic.update({'id': topic_dict['id']}, topic_dict, True)
#
#     def copy_data_to_engine():
#         file2 = '/mnt/data/liqiu/SOUCANF_APP/{}'.format(filename)
#         if os.path.getsize('{}'.format(file2)):
#             cmd = "scp -r {} tanliqiu@172.26.26.133:/home/search/ytt/search1/raw_data/src_data/".format(file2)
#             pexpect.run(cmd)
#         else:
#             pass
#
#     def dict_list(, li1):
#         li_sort = sorted(li1, key=operator.itemgetter('score'), reverse=True)
#         li_1 = []
#         if li1 != []:
#             for i in li_sort:
#                 words = i.get('tag', '')
#                 li_1.append(words)
#         return li_1
#
#     def run():
#         get_mongo()
#
#
# if __name__ == '__main__':
#     app = APP_data()
#     app.run()
#
#
#
#
#
#
#
#
#
#
#
