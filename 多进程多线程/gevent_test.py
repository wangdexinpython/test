# import gevent
#
# def func1():
#     print("start func1")
#     gevent.sleep(1)
#     print("end func1")
#
#
# def func2():
#     print("start func2")
#     gevent.sleep(1)
#     print("end func2")
#
# gevent.joinall(
#     [
#         gevent.spawn(func1),
#         gevent.spawn(func2)
#     ]
# )


import requests,json
url = 'http://39.98.194.203:8210/dailypops/v1/article/create_article'
data = {
    'data': 1,
    'stuts': 0,
    'token': 'aaqw'
}
response = requests.post(url=url, data=json.dumps(data))
