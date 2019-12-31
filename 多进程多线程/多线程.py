import _thread
# import time,queue
# q = queue.Queue
# def print_time():
#     for i in range(1,222222222):
#         time.sleep(0.5)
#         # print_data(i)
#         q.put(i)
# def print_data(data):
#     print('数据',data)


#!/usr/bin/python3

import queue
import threading
import time
exitFlag = 0
class myThread (threading.Thread):
    def __init__(, threadID, name, q):
        threading.Thread.__init__()
        threadID = threadID
        name = name
        q = q
    def run():
        print ("开启线程：" + name)
        process_data(name, q)
        print ("退出线程：" + name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")

