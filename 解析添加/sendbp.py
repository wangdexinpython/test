import requests,re,time,json


url = 'https://a.sendbp.com/redui/article/188705/947202bf3f74'
headers = {
    'Cookie': 'JSESSIONID=CBC3F3908BC7809ECDBC6370837FE4D3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
response = requests.get(url, headers=headers)
# print(response.text)
content = re.findall('vue.pageData(.*?)}\);',response.text)
print(content)