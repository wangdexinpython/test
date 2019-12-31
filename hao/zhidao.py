
import requests
import re


class zhidao(object):

    def __init__():
        url = "https://zhidao.baidu.com/uteam/ajax/answer?teamId=322&pn={}&rn=50&type=0"
        # url1 = "https://zhidao.baidu.com/uteam/contribute?teamId=322"

        # url = "https://zhidao.baidu.com/uteam/ajax/answer?teamId=322&pn=250&rn=50&type=0"
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
            "Referer":"https://zhidao.baidu.com/uteam/contribute?teamId = 322",
            "Host":"zhidao.baidu.com",
            "Cookie":"BAIDUID=81E65BFEC53F2F56491F697242B9C8AB:FG=1; BDUSS=mRmcFp6VnlneGVIMkN6WmN0eGhXQTRua09veE5mWH41MDh0YzNXeVRBTnliSnhjQVFBQUFBJCQAAAAAAAAAAAEAAACW0HPHeWVhcsO7xOO6w8TRuf0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHLfdFxy33Rca;"

        }

    def parse():
        for i in range(0,5000,50):
            url = url.format(i)
            print(url)
            html = requests.get(url,headers = headers)
            print(html.text)



    def run():
        parse()




if __name__ == '__main__':
    zhi = zhidao()
    zhi.run()