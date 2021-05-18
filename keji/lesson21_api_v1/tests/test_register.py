"""测试注册功能。

自动化测试用例。

模块名称为什么要以 test开头
测试用例函数要以 test_
"""
import requests
from common.logger_handler import get_logger

# TODO: 路径路径
logger = get_logger()


def test_register_01():
    """注册用例。"""
    # 准备测试数据
    actual_url = 'http://api.lemonban.com/futureloan/member/register'
    actual_method = 'POST'
    actual_json = {"mobile_phone":"","pwd":""}
    actual_headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    expected = 2

    # requests.request ，而不用 post
    # 访问接口
    resp = requests.request(method=actual_method,
                     url=actual_url,
                     headers=actual_headers,
                     json=actual_json)
    # 获取响应体：json
    resp_body = resp.json()

    # 断言
    try:
        assert resp_body['code'] == expected
    except AssertionError as e:
        logger.error("用例失败:{}".format(e))
        # 一定要记得抛出
        raise e


# 数据驱动
# Excel存储用例
# 封装 logger
# 配置文件的编写
# 报告
# 程序入口

# 夹具，
# 结果发送钉钉。
# 手机号码动态变化
