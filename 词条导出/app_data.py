from bson.objectid import ObjectId
import pymongo,pymysql,time,requests,os
import urllib.parse,json,pexpect
class APP_data(object):
    def __init__():
        mys=mysqldb()
        mog=mongodb()
    def get_mongo():
        cur = mys.cursor()
        count=mog.contents.find({'state_qiu':{'$exists': False}}).count()
        #count=mog.contents.find({}).count()
        print(count)
        if count>0:
            filetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
            filename = 'inc_app_{}.dat'.format(filetime)
            f = open(r'/mnt/data/liqiu/SOUCANF_APP/{}'.format(filename),'a',encoding='utf-8')
            webnum = mog.contents.find({'state_qiu':{'$exists': False}})
            #webnum = mog.contents.find({})
            for one in webnum:
                liqiu_dict={}
                if str(one['uid'])=="0.0":
                    pass
                else:
                    liqiu_dict = {'id':str(one['_id']),'uid': str(one['uid']),'link':str(one['_id']),'title': one['title'],'content': one['content'],
                              'source':'user', 'create_time': str(one['create_time']),
                             'flag':'0'}
                    liqiu_dict['crawl_time']=liqiu_dict['create_time'][0:10]
                    if one.get('bilstm_category',[]) and isinstance(one['bilstm_category'], list):
                        types=one['bilstm_category']
                        liqiu_dict['type'] = types[0]['tag']
                    elif one.get('bilstm_category','') and isinstance(one['bilstm_category'],str):
                        liqiu_dict['type'] = one['bilstm_category']
                    else:
                        liqiu_dict['type'] = ''
                    sql='''select id from album where uid="{}"'''.format(liqiu_dict['uid'])
                    cur.execute(sql)
                    num = cur.fetchall()
                    dd=[]
                    for i in num:
                        if i:
                            dd.append(str(i[0]))
                    liqiu_dict['album_id'] = ' '.join(dd)
                    url = 'http://172.26.26.135:8995/topic?content={}'.format(liqiu_dict['content'])
                    ai = requests.get(url).text
                    print(ai)
                    if ai == 'AI':
                        ai = 'ai'
                    else:
                        ai = ''
                    liqiu_dict['topic'] = ai
                    #s1 = {'_id': ObjectId(one['_id'])}
                    #s2 = {'$set': {'state_qiu': 1}}
                    #mog.contents.update(s1, s2)
                    f.write('{}\n'.format(json.dumps(liqiu_dict, ensure_ascii=False)))
            return filename
    def mongodb():
        mongo = pymongo.MongoClient(
            "mongodb://integrate:" + urllib.parse.quote_plus("integ_190228_snv738v8220aiVK9V820@_eate")+"@172.26.26.132:20388/integrate")['integrate']
        return mongo
    def mysqldb():
        connsql = pymysql.connect(host='172.26.26.132', port=3309, user='sc_read',
                                  password='S_20@ha19cxtag08)510^Y',                              db='sc', charset='utf8')
        return connsql

    def copy_data(,filename):
        file2 = '/mnt/data/liqiu/SOUCANF_APP/{}'.format(filename)
        if os.path.getsize('{}'.format(file2)):
            cmd = "scp -r {} root@172.26.26.133:/home/search/ytt/search1/raw_data/".format(file2)
            #cmd = "scp -r {} /mnt/data/liqiu/".format(file2)
            pexpect.run(cmd)
        else:
            pass
    def mv_data(,filename):
        file2 = '/mnt/data/liqiu/SOUCANF_APP/{}'.format(filename)
        if os.path.getsize('{}'.format(file2)):
            cmd = "mv {} /mnt/data/liqiu/SOUCANF_APP/data/".format(file2)
            # cmd = "scp -r {} /mnt/data/liqiu/".format(file2)
            pexpect.run(cmd)
        else:
            pass
    def run():
        filename = get_mongo()
        copy_data(filename)

if __name__ == '__main__':
    app=APP_data()
    app.run()