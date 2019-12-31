import requests

url = "http://127.0.0.1:8207/ner"
data = {"content":"""A Long March-11 carrier rocket launches five new remote-sensing satellites from the Jiuquan Satellite Launch Center in northwest China's Gobi Desert on Thursday, September 19, 2019. [Photo: China Plus/Wang Jiangbo]
The five satellites were launched by a Long March-11 carrier rocket at 2:42 p.m. (Beijing Time).
The satellites belong to a commercial remote-sensing satellite constellation project "Zhuhai-1," which will comprise 34 micro-nano satellites, including video, hyperspectral, and high-resolution optical satellites, as well as radar and infrared satellites.
The carrier rocket was developed by the China Academy of Launch Vehicle Technology, and the satellites were produced by the Harbin Institute of Technology and operated by the Zhuhai Orbita Aerospace Science and Technology Co. Ltd.
Thursday's launch was the 311th mission for the Long March series carrier rockets."""}
res = requests.post(url,data=data)
print(res.text)









