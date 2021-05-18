# get
# post

import requests

url = 'http://httpbin.org/post?username=gaoyang&password=123456'
headers = {'qq':'nana'}
resp = requests.post(url,headers=headers)
#json
print(resp.json())
#HTML,XML
print(resp.text)
#二进制数据（视频，图片）
print(resp.content)


print('-------------------------另一种方法-------------------------------')
url = 'http://httpbin.org/post?username=gaoyang&password=123456'
headers = {'qq':'nana','content-type':'application/json'}
data={'age':'15'}
resp = requests.post(url,headers=headers,json=data)
#json
print(resp.json())
#HTML,XML
print(resp.text)
#二进制数据（视频，图片）
print(resp.content)