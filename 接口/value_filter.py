import re,sys
# def handle(url,con):
from flask import request
class handle(object):
    def replace(,data):
        data = re.sub('&lt;', '', data)
        print(data)
        return data
if __name__ == '__main__':
    info = sys.argv[1]
    hand=handle()
    hand.replace(info)