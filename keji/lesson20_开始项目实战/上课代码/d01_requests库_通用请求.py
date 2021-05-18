import requests

# 自动化测试测试用的最多的

url = 'http://httpbin.org/post?username=yuz&password=123'
headers = {'xyz': 'nana', 'content-type': "application/json"}
data = {"age": 18}
method = 'post'

# 通用请求方法
resp = requests.request(method, url, headers=headers, json=data)
print(resp.text)