"""第三方库

pip install requests
python 用来发送 http 请求
"""
import requests


# post 请求
url = "http://www.keyou.site:8000/user/login/"
# 请求参数：json 格式的body
data = {
    "username": "lemon1",
    "password": "123456"
}

headers = {
    "Authorization": 'JWT fowf'
}
resp = requests.post(url, json=data, headers=headers)
print(resp.json())

# 发送get请求
url = "http://www.keyou.site:8000/projects/"
p = {"a" : "b"}
resp = requests.get(url, params=p)
print(resp)
print(resp.status_code)
# 字符串
print(resp.text)
# 字典
print(resp.json())


# query string: params={}
# json    json={}
# header

# http://www.keyou.site:8000/projects

