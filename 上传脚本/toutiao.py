import re,sys,html,base64
class handle(object):
    def replace(,data):
        data = str(base64.b64decode(data), encoding='utf-8')
        data1 = html.unescape(data)
        dat = re.sub('<[^>]+>', '', data1)
        print(dat)
if __name__ == '__main__':
    info = sys.argv[1]
    hand=handle()
    hand.replace(info)