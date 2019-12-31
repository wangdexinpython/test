#coding=utf-8
import pymongo,time,requests,json
import urllib.parse
import redis,pexpect,os
class zhidao(object):
    def __init__():
        mongo=mongodb()
        mon_app=app_mongo()

    def mongodb():
        mongo = pymongo.MongoClient(
            "mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"@172.26.26.132:20388/webpage")['webpage']
        return mongo
    def app_mongo():
        mon = pymongo.MongoClient("mongodb://integrate:" + urllib.parse.quote_plus(
                "integ_190228_snv738v8220aiVK9V820@_eate") + "@172.26.26.132:20388/integrate")
        return mon

    def Baike():
        webnum = mongo.zhidao_details.find({'state_qiu':0,'source':'baiduzhidao'}).count()
        print(webnum)
        if webnum>0:
            filetime = time.strftime("%Y%m%d", time.localtime())
            filename = 'inc_zhidao_{}.dat'.format(filetime)
            # filename = 'inc_zhidao_20190527.dat'
            f = open(r'/mnt/data/liqiu/zhidao/{}'.format(filename),'a',encoding='utf-8')
            for i in range(0,webnum,10000):
                print('*****************************************',i)
                # filetime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
                # filename = 'full_{}.dat'.format(filetime)
                # f = open(r'/mnt/data/liqiu/{}'.format(filename),'a',encoding='utf-8')
                zds = mongo.zhidao_details.find({'state_qiu':0,'source':'baiduzhidao'}).limit(10000).skip(i)
                for one in zds:
                    try:
                        liqiu_dict = {'id':str(one['id']),'link':str(one['id']),'title':str(one['title']),'author':str(one['author']),'content':str(one['content_np']),'site_name':str(one['site_name']),'article_url':str(one['article_url']),'crawl_time':str(one['crawl_time']),'source':str(one['source']),'topic':'','flag':'0'}
                        if one.get('type',[]) and isinstance(one['type'],list):
                            liqiu_dict['type']=' '.join(one['type'])
                        elif one.get('type','') and isinstance(one['type'],str):
                            liqiu_dict['type']= one['type']
                        else:
                            liqiu_dict['type']=''
                        if one.get('label',[]) and isinstance(one['label'],list):
                            liqiu_dict['label']=' '.join(one['label'])
                        elif one.get('label',"") and isinstance(one['label'],str):
                            liqiu_dict['label']= one['label']
                        else:
                            liqiu_dict['label']=''
                        # if len(liqiu_dict)==0:
                        #     continue
                        cons = liqiu_dict['content']
                        url = 'http://172.26.26.135:8995/topic?content={}'.format(cons)
                        ai = requests.get(url).text
                        print(ai)
                        if ai == 'AI':
                            ai = 'ai'
                        else:
                            ai = ''
                        liqiu_dict['topic'] = ai
                        read_dat(liqiu_dict)
                        f.write('{}\n'.format(json.dumps(liqiu_dict,ensure_ascii=False)))
                        s1={'id':one['id']}
                        s2 = {'$set':{'state_qiu':1}}
                        mongo.zhidao_details.update(s1,s2)
                    except KeyError as e:
                        print('异常')
                        print('---------------------------',e)
                        # continue
                    # f.write('{}\n'.format(json.dumps(liqiu_dict,ensure_ascii=False)))
    def read_dat(,line):
        if line['topic'] == 'ai':
            dict_1 = {'id': line['id'], 'content': line['content'], 'crawl_time': line['crawl_time'],
                      'title': line['title'], 'source': line['source'], 'topic': line['topic'], 'type': line['type'],
                      'url': line['article_url']}
            try:
                dict_1['label'] = line['label']
            except:
                dict_1['label'] = ''
                # print(dict_1)
            mon_app.integrate.data_dat.update({'id': dict_1['id']}, dict_1, True)
    def copy_data():
        fileti = time.strftime("%H%M%S", time.localtime())
        if int(fileti) > 230000:
            # 判断文件是否为空
            filetime = time.strftime("%Y%m%d", time.localtime())
            filename = 'inc_zhidao_{}.dat'.format(filetime)
            file2 = '/mnt/data/liqiu/zhidao/{}'.format(filename)
            if os.path.getsize('{}'.format(file2)):
                # 将写好的文件scp到指定文件夹下
                cmd = "scp -r {} root@172.26.26.133:/home/search/ytt/search1/raw_data/src_data/".format(file2)
                pexpect.run(cmd)
            else:
                pass
    def run():
        Baike()
        copy_data()
if __name__ == '__main__':
    zhi=zhidao()
    zhi.run()
