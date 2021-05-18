"""测试注册功能

自动化测试用例

要以test开头

"""

import requests

from common.logger_handler import get_logger
logger = get_logger()


def test_register_01():
    """注册用例"""
    url = 'http://api.lemonban.com/futureloan/member/register'
    method = 'POST'
    json = {"mobile_phone":"","pwd":""}
    headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    expected = 2

    resp = requests.request(method=method,
                            url=url,
                            headers=headers,
                            json=json)

    # 获取响应体：json
    resp_body = resp.json()

    # 断言和日志
    try:
        assert resp_body['code'] == expected
    except AssertionError as e:
        logger.error("用例失败:{}".format(e))
        #一定要记得抛出
        raise e

#数据驱动
#Excel
#封装 logger
#配置文件的编写
#报告
#入口
#夹具
#结果发送钉钉
#随机数（手机号）


