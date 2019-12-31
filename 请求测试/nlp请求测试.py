import requests

url = "http://192.168.0.129:8208/abstract"  # 摘要
# url = "http://192.168.56.1:8208/keywords"   # 关键字

querystring = {"content":"""The Pacific island nation of Kiribati on Friday abruptly severed "diplomatic ties" with Taiwan. It came less than a week after the Solomon Islands cut "diplomatic ties" with Taiwan. Taiwan's "diplomacy" is collapsing, and may lose all of its "allies."

Kiribati established diplomatic relations with the People's Republic of China in 1980, but the Taiwan authority bought over its "diplomatic ties" in 2003. At that time, Taiwan's GDP was about one-fifth of the mainland's, and Taiwan could adopt "money diplomacy." But after more than 10 years, Taiwan's GDP is less than one-twentieth of the mainland's. Such "money diplomacy" has collapsed in Taiwan.

The Taiwan authority declared that the mainland used money to buy over Pacific nations. But these nations required no financial assistance when they switched to the mainland. Because of short-term economic interests, these nations used to maintain "diplomatic ties" with Taiwan. They are now propelled by strategic interests to establish ties with the mainland. After all, a country will seem strange if it has no diplomatic relations with the mainland.

In the globalization era, Taiwan's financial assistance has become less attractive to the smaller nations as the Chinese mainland-proposed Belt and Road Initiative expands coverage. Smaller nations need sustainable development conditions rather than temporary alms from a region which is politically suspicious in it
"""}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "5e871933-1b03-47e5-8224-117687cc7a8f"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)