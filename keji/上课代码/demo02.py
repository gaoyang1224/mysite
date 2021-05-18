import requests

def send_request(url, method, data=None, header=None, json=None, **kw):
    """封装发送请求的代码"""
    resp = requests.request(method=method,
                     url=url,
                     data=data,
                     headers=header,
                     json=json, **kw)
    try:
        ret = resp.json()
    except:
        ret = resp.text
    return url


class HTTP:
    # def __init__(self):
    #     pass

    def send_request(self, url, method, data=None, header=None, json=None, **kw):
        """封装发送请求的代码"""
        resp = requests.request(method=method,
                                url=url,
                                data=data,
                                headers=header,
                                json=json, **kw)
        try:
            ret = resp.json()
        except:
            ret = resp.text
        return url

    def get(self):
        return self.send_request(method='get')

    def post(self):
        return self.send_request(method='post')



a = send_request('http://api.lemonban.com/futureloan/member/register', 'post')
print("函数的返回值", a)



