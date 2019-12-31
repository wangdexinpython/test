

# import requests
# ACCESS_TOKEN = "24.b37a10716f8c54dd16f2218d9daf6d5b.2592000.1553671382.282335-15048976"
# def baiduapi(word):
#     url = "https://aip.baidubce.com/rpc/2.0/kg/v1/cognitive/entity_annotation?access_token={}".format(ACCESS_TOKEN)
#     headers = {
#         "content-type":"application/json",
#         "expires_in":"259200000",
#     }
#     data = '{{"data":"{}"}}'.format(word)
#     byte_data = data.encode('utf-8')
#     response2 = requests.post(url=url,headers=headers,data=byte_data)
#     return response2.content.decode()


# def str_dict(str):
#     li1 = str.split(' ')
#     print(li1)
#     b=''.join(li1)
#     print('ss',type(b))
#     # return li1
# a=''
# str_dict(a)

# s='    通信技术'
# s=''
# s1 = s.strip()
# print(s1)

from urllib.parse import urlparse
ss = urlparse('').netloc
print('ss',ss)





