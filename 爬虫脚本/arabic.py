import requests,json,time
url='https://www.alarabiya.net/ar/latest-news/mainArea/0/mainContent/00/pArea75/0?&pageNo=1'

headers={"Cookie":"NEW_VISITOR=new; VISITOR=returning; YPF8827340282Jdskjhfiw_928937459182JAX666=118.187.53.6; JSESSIONID=CE668EA32001C00F98F2038A708FD8F5; dis-request-id=b9a5d7b926a1c7a650849a5bbceca1aa; dis-timestamp=2019-12-02T22:44:07-08:00; dis-remote-addr=118.187.53.6"}

html=requests.get(url,headers=headers).text
print(html)



import scrapy

class arabic(scrapy.Spider):
    name = 'arab'
    custom_settings = {
        "Cookies_enabled":False,
    }

    def start_requests():
        url="https://www.alarabiya.net/ar/latest-news/mainArea/0/mainContent/00/pArea75/0?&pageNo=1"

        yield scrapy.Request(callback=url,cookies={"Cookie":"NEW_VISITOR=new; VISITOR=returning; YPF8827340282Jdskjhfiw_928937459182JAX666=118.187.53.6; JSESSIONID=CE668EA32001C00F98F2038A708FD8F5; dis-request-id=b9a5d7b926a1c7a650849a5bbceca1aa; dis-timestamp=2019-12-02T22:44:07-08:00; dis-remote-addr=118.187.53.6"})

