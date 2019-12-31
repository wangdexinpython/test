import threading,time
def dosomething(da):
    print(da)
while True:
    time.sleep(1)
    for i in range(0,10):
        t=threading.Thread(target=dosomething,args=(i,))
        t.setDaemon(True)
        t.start()
    t.join()