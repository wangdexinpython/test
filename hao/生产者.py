import threading, time, queue,requests,json
li1 = []
def Produce():
    while True:
        time.sleep(1)
        proxy = requests.get(
            url="http://d.jghttp.golangapi.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=").text
        pro = json.loads(proxy)
        if pro['data'] != []:
            proxy_ip = (pro['data'][0]["ip"])
            proxy_port = (pro['data'][0]["port"])
            ip_port = proxy_ip + ":" + proxy_port
            proxy = {
                'https': ip_port
            }
            if li1==[]:
                li1.append(proxy)
            else:
                li1[0] = proxy
def Consumer():
    while True:
        if  li1 !=[]:
            print(li1[0])
if __name__ == '__main__':
    p1 = threading.Thread(target=Produce)
    c1 = threading.Thread(target=Consumer)
    print("999999999")
    p1.start()
    c1.start()
