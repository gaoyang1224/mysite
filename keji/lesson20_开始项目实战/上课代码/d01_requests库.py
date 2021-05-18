"""
- get
- post
"""
import requests

# 发送 GET 请求
# 接口地址： 本地 http://host:port/user/login
# 写代码之前，先用 postman 手工测一把

url = 'http://httpbin.org/get'
headers = {'xyz': 'nana'}
data = {"username": "yuz", "password": "123"}
resp = requests.get(url, params=data, headers=headers)
print(resp.json())
# HTML, XML
print(resp.text)
# 二进制的数据， 图片，视频， bytes
print(resp.content)