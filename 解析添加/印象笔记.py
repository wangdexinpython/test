import json

import requests
from lxml import etree
import re,base64
# &
# $fb617cac-680e-4c19-926a-50a2548d2ff7
# AAAAACYK
def get_url(url):
    if 'bitan.app.yinxiang.com' in url:
        url_sp = '$'+ url.split('/')[-1]
        url_base64 = base64.b64encode(url_sp.encode('utf-8'))
        url_base64 = str('AAAAACYK'+url_base64.decode())

        url_api = 'https://app.yinxiang.com/officialNotebook/gRPCWeb/official.OfficialNotebookService/GetNote'
        headers = {
            'Content-Type': 'application/grpc-web-text'
        }
        print('data',url_base64)
        # response_api = requests.post(url=url_api, data=url_base64,headers=headers).text
        response_api = requests.post(url=url_api, data="AAAAACYKJGZiNjE3Y2FjLTY4MGUtNGMxOS05MjZhLTUwYTI1NDhkMmZmNw==",headers=headers).text

        content = re.findall('<div class="ennote">(.*)</div>',response_api)[0]
        content = re.sub('<[^>]+>', '', content)
        print(content)

if __name__ == '__main__':
    get_url(url = 'https://bitan.app.yinxiang.com/official/note/fb617cac-680e-4c19-926a-50a2548d2ff7')