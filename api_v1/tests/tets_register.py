"""
注册功能
"""
from common.logger_handler import logger
import requests

logger = logger('demo.log')

def test_register_01():
    url = 'http://api.lemonban.com/futureloan/member/register'
    method = 'post'
    headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    json = {"mobile_phone": "", "pwd": ""}
    expected = 2
    # 访问接口
    resp = requests.request(method=method,
                            url=url,
                            headers=headers,
                            json=json)
    # 获取响应体json
    resp_body = resp.json()
    # 断言
    try:
        assert resp_body['code'] == expected
    except AssertionError as e:
        logger.error("用例失败{}".format(e))
        # 抛出异常
        raise e
