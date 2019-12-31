
import pymysql

def mysqldb():
    connsql = pymysql.connect(host='hdm117265566.my3w.com', port=3306, user='hdm117265566', password='uuQdkyYoyb6fZqOm',
                              db='hdm117265566_db', charset='utf8')
    return connsql
# conn=mysqldb()
#
# cursor = conn.cursor()
# sql = '''select * from section'''
# num = cursor.execute(sql)
# print('num',num)

connsql = mysqldb()
cur = connsql.cursor()
sql='''select * from section where length(content_parse)>50 limit {} offset {}'''.format(3,0)
cur.execute(sql)
content = cur.fetchall()
connsql.close()
print('num',content)

