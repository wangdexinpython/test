import requests,json
url = "http://127.0.0.1:8210/dailypops/v1/article/create_article"

data = {
    'data': 1,
    'stuts': 0,
    'token': 'aaqw'
}
response = requests.post(url=url, data=json.dumps(data))




