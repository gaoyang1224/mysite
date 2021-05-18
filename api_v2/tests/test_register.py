"""
注册功能
"""
import os

from common.logger_handler import logger
from common.excel_handler import ExcelHandler
import requests
import pytest
from config import path
from common.yaml_handler import yaml_config
from common.helper import generate_new_phone

excel_file = os.path.join(path.data_path, 'cases.xlsx')
data = ExcelHandler(excel_file).read('register')


@pytest.mark.parametrize("test_info", data)
def test_register_01(test_info):
    url = test_info['url']
    method = test_info['method']
    headers = test_info['headers']
    json = test_info['json']
    expected = test_info['expected']

    if "#new_phone#" in json:
        phone = generate_new_phone()
        json = json.replace('#new_phone#', phone)

    # 访问接口
    resp = requests.request(method=method,
                            url=yaml_config["host"] + url,
                            headers=eval(headers),
                            json=eval(json))
    # 获取响应体json
    resp_body = resp.json()
    # 断言
    try:
        assert resp_body['code'] == expected
    except AssertionError as e:
        logger.error("用例失败{}".format(e))
        # 抛出异常
        raise e
    # # 写入数据
    # finally:
    #     excel = ExcelHandler(excel_file)
    #     excel.write('register',
    #                 str(resp_body),
    #                 row=int(test_info['case_id']) + 1,
    #                 column=9)
