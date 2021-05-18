"""测试注册功能。

自动化测试用例。

模块名称为什么要以 test开头
测试用例函数要以 test_
"""
import requests
import pytest
from common.logger_handler import logger
from common.excel_handler import ExcelHandler


import os
from config import path

# log_file = os.path.join(path.logs_path, 'py36.log')
# logger = get_logger(file=log_file)

# 获取excel文件的路径
excel_file = os.path.join(path.data_path, 'cases.xlsx')
data = ExcelHandler(excel_file).read('register')

@pytest.mark.parametrize("test_info", data)
def test_register_01(test_info):
    """注册用例。"""
    # 准备测试数据
    # actual_url = 'http://api.lemonban.com/futureloan/member/register'
    # actual_method = 'POST'
    # actual_json = {"mobile_phone":"","pwd":""}
    # actual_headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    # expected = 2
    actual_url = test_info['url']
    actual_method = test_info['method']
    actual_json = test_info['json']
    actual_headers = test_info['headers']
    expected = test_info['expected']
    # requests.request ，而不用 post
    # 访问接口
    resp = requests.request(method=actual_method,
                     url=actual_url,
                     headers=eval(actual_headers),
                     json=eval(actual_json))
    # 获取响应体：json
    resp_body = resp.json()

    # 断言
    try:
        assert resp_body['code'] == expected
    except AssertionError as e:
        logger.error("用例失败:{}".format(e))
        # 一定要记得抛出
        raise e


# 数据驱动 DONE
# Excel存储用例 DONE
# 封装 logger DONE
# 配置文件的编写 UNDONE
# 报告 DONE
# 程序入口  DONE

# 夹具，UNDONE
# 结果发送钉钉。
# 手机号码动态变化
