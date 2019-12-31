import rsa
import binascii
import random
from PIL import Image
import base64
import urllib3
from urllib.parse import urlparse
import requests
import hashlib
import json
import time
import re
from hashlib import md5
from lxml import etree

class Weibo(object):
    def __init__(self,user_name, pass_word, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.dama_headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
        self.session = requests.session()
        self.user_name = user_name
        self.pass_word = pass_word
        self.headers = {
            'Host': 'login.sina.com.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Referer': 'https://weibo.com/',
        }

    def get_input_username(self):
        url = 'https://login.sina.com.cn/sso/prelogin.php'
        su = self.get_username()
        params = {
            'su':su,
            'rsakt':'mod',
            'entry':'weibo',
            'client':'ssologin.js(v1.4.19)',
            'checkpin':1,
            'callback':'sinaSSOController.preloginCallBack',
            '_':int(time.time() * 1000)
        }
        # 获取json数据,参数
        response = self.session.get(url, params=params, verify=False).text
        text = re.findall('{.*?}',response)[0]
        json_data = json.loads(text)
        self.pubkey = json_data['pubkey']
        self.nonce = json_data['nonce']
        self.rsakv = json_data['rsakv']
        self.servertime = json_data['servertime']
        self.pcid = json_data['pcid']

    # rsa加密
    def get_password(self):
        pubkey = rsa.PublicKey(int(self.pubkey,16),int('10001',16))
        s = str(self.servertime) + '\t' + str(self.nonce) + '\n' + str(self.pass_word)
        password = rsa.encrypt(s.encode(),pubkey)
        return binascii.b2a_hex(password)

    # 获取验证码并打码
    def get_picture(self):
        data = {
            'r':'484442' + str(random.randint(10,99)),
            's':'0',
            'p':self.pcid,
        }
        picture = self.session.get(
            'https://login.sina.com.cn/cgi/pin.php?r=48444256&s=0&p=tc-484b6d0677afb4fca906d3dc042c2a035c26',params=data).content
        with open('./a.jpg', 'wb') as f:
            f.write(picture)

        # im = Image.open('a.jpg')
        # im.show()
        im = open('./a.jpg', 'rb').read()
        params = {
            'codetype': 1902,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.dama_headers).text
        js = json.loads(r)
        verify_num = js.get('pic_str','')
        return verify_num

    def ReportError(self, im_id):
        # im_id:报错图片ID
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.dama_headers)
        return r.json()

    # 得到base64编码后的密码
    def get_username(self):
        return base64.encodebytes(self.user_name.encode()).decode().rstrip()

    # 代理ip
    def get_proxies(self):
        ip_url = 'http://d.jghttp.golangapi.com/getip?num=1&type=2&pro=110000&city=110105&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        response = requests.get(url=ip_url).text
        js = json.loads(response)['data'] and json.loads(response)['data'][0] or ""
        ip = js.get('ip', '')
        port = js.get('port', '')
        proxyMeta = "http://%(host)s:%(port)s" % {
            "host": ip,
            "port": port,
        }
        proxies = {
            "https":proxyMeta
        }
        return proxies

    # 登录
    def login(self):
        proxies = self.get_proxies()
        self.get_input_username()
        su = self.get_username()
        sp = self.get_password()
        # 登录地址
        url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
        verify_num = self.get_picture()
        data ={
            'entry':'weibo',
            'gateway':1,
            'from':'',
            'savestate':7,
            'qrcode_flag':'false',
            'useticket':1,
            'pagerefer':'https://www.baidu.com/link?url=EGHg5FQCDTZHAqPp2loYjvBWnt9RrpCKAWxTdmd4ZsS&wd=&eqid=bde599aa00043f74000000055ad434aa',
            'vsnf':1,
            'su':su,
            'service':'miniblog',
            'servertime':self.servertime,
            'nonce':self.nonce,
            'pwencode':'rsa2',
            'rsakv':self.rsakv,
            'sp':sp,
            'sr':'1920*1080',
            'encoding':'UTF-8',
            'prelt':536,
            'url':'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype':'META',
            'pcid':self.pcid,
            'door':verify_num
        }
        response = self.session.post(url,data=data).content.decode('GBK')
        url1 = re.findall('location.replace\("(.*?)"\)',response)[0]

        # 登录界面
        response = self.session.get(url=url1).content.decode('gbk')

        url2 = re.findall("location.replace\('(.*)'\)",response)[0]

        try:
            response = self.session.get(url=url2, proxies=proxies).content.decode('gbk')
            # 获得用户id
            self.uid = json.loads(re.findall('feedBackUrlCallBack\((.*)\)', response)[0])['userinfo']['uniqueid']
        except:
            return self.login()

        url3 = 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&sudaref=weibo.com'
        self.session.get(url=url3, verify=False).content.decode('gbk')

        self.session.get('https://weibo.com/?wvr=5&lf=reg')

        # 进入主页
        url4 = 'https://weibo.com/u/{}/home?wvr=5&lf=reg'.format(self.uid)
        self.session.get(url4).content.decode()

    def get_session(self):
        session = requests.session()
        session.cookies = weibo.session.cookies
        return session

    # 登录后cookie


    # 文章url
    def get_url(self):
        url="https://card.weibo.com/article/m/show/id/2309404363550268218951?_wb_client_=1&from=groupmessage"
        session = self.get_session()
        url_id = re.findall('http.*?id/(\d+)', url) and re.findall('http.*?id/(\d+)', url)[0] or ""
        url_api = 'https://weibo.com/ttarticle/p/show?id={}'.format(url_id)
        response = session.get(url=url_api)
        print(response.text)
        # return response.text


if __name__ == '__main__':
    weibo = Weibo('zhaoqiang_zq@126.com', '1!aA123','13439303439', 'cjp106387', '901969')
    weibo.login()
    weibo.get_proxies()
    weibo.get_session()
    print(weibo.get_url())


