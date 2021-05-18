# get
# post

import requests

url = 'http://httpbin.org/get?username=gaoyang&password=123456'
headers = {'qq':'nana'}
resp = requests.get(url,headers=headers)
#json
print(resp.json())
#HTML,XML
print(resp.text)
#二进制数据（视频，图片）
print(resp.content)


print("-----------------另一方法-----------------------")
url = 'http://httpbin.org/get'
headers = {'qq':'nana'}
date = {'username':'gaoyang','password':'123456'}
resp = requests.get(url,params=date,headers=headers)
#json
print(resp.json())
#HTML,XML
print(resp.text)
#二进制数据（视频，图片）
print(resp.content)

