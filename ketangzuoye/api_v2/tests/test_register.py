"""测试注册功能

自动化测试用例

要以test开头

"""
import os
import pytest
import requests

from common.excel_headler import ExcelHandler
from common.logger_handler import logger
from common.yaml_handler import yaml_config
from common.helper import generate_new_phone

# log_file = os.path.join(path.logs_path, 'py36.log')
# logger = get_logger(file=log_file)

# 获取Excel路径
from config import path

excel_file = os.path.join(path.data_path, 'cases.xlsx')
data = ExcelHandler(excel_file).read('register')


@pytest.mark.parametrize("test_info", data)
def test_register_01(test_info):
    """注册用例"""
    # url = 'http://api.lemonban.com/futureloan/member/register'
    # method = 'POST'
    # json = {"mobile_phone": "", "pwd": ""}
    # headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
    # expected = 2

    method = test_info['method']
    url = test_info['url']
    json = test_info['json']
    headers = test_info['headers']
    expected = test_info['expected']

    # 读取 test_info['json']
    # 如果存在#new_phone#
    if '#new_phone#' in json:
        # 生成手机号码 generate_new_phone
        # 15195989875 替换 #new_phone#
        phone = generate_new_phone()
        json = json.replace('#new_phone#', phone)

    if '#exist_phone#' in json:
        phone = generate_new_phone()
        json = json.replace('#exist_phone#', phone)

    resp = requests.request(method=method,
                            url=yaml_config['host'] + url,
                            headers=eval(headers),
                            json=eval(json))
    print(json)

    # 获取响应体：json
    resp_body = resp.json()

    # 断言和日志
    try:
        assert resp_body['code'] == expected
    except AssertionError as e:
        logger.error("用例失败:{}".format(e))
        # 一定要记得抛出
        raise e

# 数据驱动
# Excel
# 封装 logger
# 配置文件的编写
# 报告
# 入口
# 夹具
# 结果发送钉钉
# 随机数（手机号）
