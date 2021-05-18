import requests


url = 'http://httpbin.org/post?username=gaoyang&password=123456'
method = 'post'
#param = {}
headers = {'qq':'nana','content-type':'application/json'}
data = {'age':'15'}

#通用的请求
resp = requests.request(method,url,headers=headers,json=data)
print(resp.json())
