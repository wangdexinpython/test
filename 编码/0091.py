import requests,re,json
headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
url='https://www.haodf.com/doctor/DE4rO-XCoLUXxbXYw1mnSzFYx4.htm'
cons  =requests.get(url,headers=headers).text
c1 = re.findall(r'<div id=\\"truncate_DoctorSpecialize\\" style=\\".*?;\\">(.*?)<\\/div>',cons)[0].replace(' ','').replace('\t','')
print(c1)
ss = c1.encode('utf-8').decode('unicode_escape').replace('\s','')
# sss =
# ss=json.loads(c1,encoding='unicode_escape')
print(ss)



