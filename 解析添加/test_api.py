import requests,re
haders = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

url='https://www.toutiao.com/group/6699212848280633868/'
response_text = requests.get(url,headers=haders).text
print('response',response_text)
artical_pat = re.compile(u"(?<=content:)[\w\W]*?(?=groupId)")
articals = artical_pat.findall(response_text) and artical_pat.findall(response_text)[0] or ""
print('articals',articals)








