# -*- coding:utf-8 -*-
import sys
sys.path.append("../../")
sys.path.append("/mnt/home/wangdexin/datapipeline/")
import time,requests,os,re
import urllib.parse,json,pexpect
from database.mongodb import MongoDB
from database.mysqldb import MysqlDB
# environment='local'
environment='server'
db_name_contents='integrate'
db_name_topic='topic'
da_name_sql='sc'
class APP_data(object):
    def __init__():
        find_time = int((time.time())*1000)-300000
        filetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filename = 'inc_app_{}.dat'.format(filetime)
        # f = open(r'./app_full.dat', 'a', encoding='utf-8')
        mog_content = MongoDB(environment=environment,db_name=db_name_contents).client
        mog_topic = MongoDB(environment=environment,db_name=db_name_topic).client
        mys=MysqlDB(environment=environment,db_name=da_name_sql).getClient()
        cur = mys.cursor()
    def get_mongo():
        count=mog_content.integrate.contents.find({'create_time':{'$gt': find_time}}).count()
        if count > 0:
            f = open(r'/mnt/data/liqiu/SOUCANF_APP/{}'.format(filename), 'a', encoding='utf-8')
            webnum = mog_content.integrate.contents.find({'create_time':{'$gt': find_time}})
            for one in webnum:
                data_return = engine_data(one)
                read_data_to_topic(data_return)
                f.write('{}\n'.format(json.dumps(data_return, ensure_ascii=False)))
                copy_data_to_engine()
    def engine_data(,data):
        engine_dict = {}
        len_num = len(str(data.get('content','')))
        if len_num > 10:
            engine_dict['id']=str(data.get('_id',''))
            engine_dict['uid']=str(data.get('uid',''))
            engine_dict['link']=str(data.get('_id',''))
            engine_dict['title']=str(data.get('title',''))
            engine_dict['content']=str(data.get('content',''))
            engine_dict['source']='user'
            engine_dict['article_url']=str(data.get('path',''))
            engine_dict['flag']='0'
            engine_dict['crawl_time']=str(data.get('create_time',''))[0:10]
            engine_dict['doc_groups'] = '' if data.get('app_album_ids', '') == '' else  str(data['app_album_ids'])
            engine_dict['label'] = label_mongo(data)
            engine_dict['topic'] = entity_mongo(data)
            engine_dict['album_id'] = get_album_id(engine_dict.get('uid',''))
            engine_dict['type'] = AI_get_nlp(engine_dict.get('content',''))
            engine_dict['data_type']='user'
            engine_dict['db']='integrate'
            engine_dict['table']='contents'
        return engine_dict
    def get_album_id(,uid):
        sql = '''select id from album where uid="{}"'''.format(uid)
        cur.execute(sql)
        num = cur.fetchall()
        dd = []
        for i in num:
            if i:
                dd.append(str(i[0]))
        return ' '.join(dd)
    def AI_get_nlp(,data):
        url = 'http://172.26.26.139:8995/topic?content={}'.format(data)
        ai = requests.get(url).text
        type_nlp = 'ai' if ai == 'AI' else ''
        return type_nlp
    def entity_mongo(,di):
        entity_=[]
        entity_.extend(dict_list(di.get('bd_entity','')))
        entity_.extend(dict_list(di.get('core_entity','')))
        entity_.extend(dict_list(di.get('bilstm_entity','')))
        entitys = list(set(entity_))
        return ' '.join(entitys)
    def label_mongo(,dic):
        app_tags=[]
        if dic.get('app_tags','')!='':
            app_tags.extend(dic.get('app_tags','').split(','))
        user_tags = dic.get("user_tags",[])
        app_tags.extend(dict_list(dic.get('bd_label','')))
        app_tags.extend(dict_list(dic.get('bd_entity','')))
        app_tags.extend(dict_list(dic.get('core_label','')))
        app_tags.extend(dict_list(dic.get('core_entity','')))
        app_tags.extend(dict_list(dic.get('bilstm_label','')))
        app_tags.extend(dict_list(dic.get('bilstm_entity','')))
        app_tags.extend(user_tags)
        label_ = list(set(app_tags))
        return ' '.join(label_)
    def read_data_to_topic(,data):
        topic_dict={}
        if data.get('type','') == 'ai':
            topic_dict['id']=data.get('id','')
            topic_dict['content']=data.get('content','')
            topic_dict['crawl_time']=data.get('crawl_time','')
            topic_dict['site']=data.get('source','')
            topic_dict['source']='soucang'
            topic_dict['AI_source']='article'
            topic_dict['topic']=data.get('type','')
            topic_dict['type']=data.get('topic','')
            topic_dict['url']=data.get('article_url','')
            topic_dict['label']=data.get('label','')
            if data.get('title','') == '':
                first_word = re.findall('^(.*?)。', data.get('content',''))
                first_dou = re.findall('^(.*?),', data.get('content',''))
                if first_word != []:
                    topic_dict['title'] = ''.join(first_word)
                elif first_dou != []:
                    topic_dict['title'] = ''.join(first_dou)
                else:
                    topic_dict['title'] = data.get('content','')
            else:
                topic_dict['title'] = data.get('title','')
            mog_topic.topic.AI_topic.update({'id': topic_dict['id']}, topic_dict, True)
    def copy_data_to_engine():
        file2 = '/mnt/data/liqiu/SOUCANF_APP/{}'.format(filename)
        if os.path.getsize('{}'.format(file2)):
            cmd = "scp -r {} tanliqiu@172.26.26.133:/home/search/ytt/search1/raw_data/src_data/".format(file2)
            pexpect.run(cmd)
        else:
            pass
    def dict_list(,li1):
        li_1=[]
        if li1!=[]:
            for i in li1:
                words=i.get('tag','')
                li_1.append(words)
        return li_1
    def run():
        get_mongo()
if __name__ == '__main__':
    app=APP_data()
    app.run()




