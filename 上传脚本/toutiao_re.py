import re,sys
class handle(object):
    def replace(,data):
        data = re.sub('&.*?;', '', data)
        print(data)
if __name__ == '__main__':
    info = sys.argv[1]
    hand=handle()
    hand.replace(info)