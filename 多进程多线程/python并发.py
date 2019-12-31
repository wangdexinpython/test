# -*- coding: utf-8 -*-
# @Time : 2019/12/10 14:24
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : python并发.py
# @Project : test
'''
pp
'''
# import asyncio
# from time import strftime
#
#
# @asyncio.coroutine
# def hello():
#     print(strftime('[%H:%M:%S]'), "Hello world!")
#     r = yield from asyncio.sleep(1)
#     print(strftime('[%H:%M:%S]'), "Hello again!")
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

import threading
import asyncio
from time import strftime


# @asyncio.coroutine
# def hello(id):
#     print(strftime('[%H:%M:%S]'), 'coroutine_id:%s thread_id:%s' % (id, threading.currentThread()))
#     yield from asyncio.sleep(1)
#     print(strftime('[%H:%M:%S]'), 'coroutine_id:%s thread_id:%s' % (id, threading.currentThread()))
#     return "id{}".format(id)
# async def hello(id):
#     print(strftime('[%H:%M:%S]'), 'coroutine_id:%s thread_id:%s' % (id, threading.currentThread()))
#     await asyncio.sleep(1)
#     print(strftime('[%H:%M:%S]'), 'coroutine_id:%s thread_id:%s' % (id, threading.currentThread()))
#     return "id{}".format(id)
#
# loop = asyncio.get_event_loop()
# tasks = [hello(id) for id in range(0,5)]
# wait_coro = asyncio.wait(tasks)
# res = loop.run_until_complete(wait_coro)
#
# print(res)
# print(len(res))
#
# loop.close()


async def get_flag(cc):
    return "num{}".format(cc)
def call_back(future):
    print("callback:", future.result())
loop = asyncio.get_event_loop()
to_do=[get_flag(cc) for cc in range(1,13)]
wait_coro = asyncio.wait(to_do)
res=loop.run_until_complete(wait_coro)
loop.close()
print(res)
print(len(res))
print(type(list(res)))
res1= list(res)[0]
print("type",type(list(res1)))
for k in list(res1):
    print(k.result())



# import time
# import asyncio
# now = lambda : time.time()
# async def do_some_work(x):
#     print("waiting:",x)
#     return "Done after {}s".format(x)
# def callback(future):
#     print("callback:",future.result())
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# print(task)
# task.add_done_callback(callback)
# print(task)
# loop.run_until_complete(task)
# print("Time:", now()-start)
