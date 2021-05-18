"""
- post
"""
import requests

# 发送 GET 请求
# 接口地址： 本地 http://host:port/user/login
# 写代码之前，先用 postman 手工测一把

url = 'http://httpbin.org/post?username=yuz&password=123'
headers = {'xyz': 'nana', 'content-type': "application/json"}

data = {"age": 18}

# requests, 如果想传递 form-data, data=a
# resp = requests.post(url, headers=headers, data=data)
# print(resp.json())
# # HTML, XML
# print(resp.text)
# # 二进制的数据， 图片，视频， bytes
# print(resp.content)


# 传递 json 数据， content-type = 'application/json',   json=data
resp = requests.post(url, headers=headers, json=data)
print(resp.json())
# HTML, XML
print(resp.text)
# 二进制的数据， 图片，视频， bytes
print(resp.content)


