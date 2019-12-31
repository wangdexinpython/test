import requests,json
url = 'https://file.wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetmedia?&mediaid=@crypt_b7418c19_7796c69a6a0979a2840326ca40c51dc3c2a75022b62ce51174e20741837ec1b962e256c9b0955a47f3b127afd8d1965df296fd8ebf37ce2b756d75122af0ce91850b981066944ff2f1220a0a9d2df2b4288301ca86ec70e534a1acb66fb88383a0ad56f67d9cc5e7546d845acede920d171cfa50ffa175f8cfe9a0d3e96e769ab9fbed138eef3ac49b5d846670a6bc28d9772a6bcf1fd9485077e9af344e6bff444f3bf5fe28f2b6935a8459c19d0eb8a0502df9032f26965749688d71c07ab14e64eb4a4bb6e668fb061ff090a80740e92eb1989b68fc47f540dd55a0603cdbc41c57babb7cd7c61df8582487fb44dc4b8201b4f30df8295f317be88808a31fdb22ae9ea06512179c3c95056e9b123db484043a7a40bb5f16b42357269fec16463bf393f8dc20f36cbaed186c912b9b&encryfilename=%E7%AC%AC6%E8%AF%BE%20%E4%BD%BF%E7%94%A8NLTK%E8%BF%9B%E8%A1%8CPython%E6%96%87%E6%9C%AC%E5%88%86%E6%9E%90%2Epdf&webwx_data_ticket=gScvsbVVZe6f4EefDIOZzE9W'
headers = {
    'Cookie': 'wxuin=3053089480;wxsid=i5k68u8hkl6thBJ7;',
}
s = requests.session()
res = s.get(url=url,headers=headers)
print(res)
try:
    with open(r'D:\test\下载pdf\1.pdf'+'qwe'+'.pdf', 'wb') as f:
        f.write(res.content)
        print("下载完成")
except Exception as e:
    print(e)


