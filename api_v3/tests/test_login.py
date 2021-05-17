import pytest
import os

import requests

from common.logger_handler import logger
from config import path
from common.excel_handler import ExcelHandler
from common.yaml_handler import yaml_config, user_config
from common.helper import generate_new_phone

excel_file = os.path.join(path.data_path, 'cases.xlsx')
data = ExcelHandler(excel_file).read('login')


@pytest.mark.parametrize('info', data)
def test_login(info):
    request_data = info['data']
    if '*phone*' in request_data:
        new_phone = generate_new_phone()
        request_data = request_data.replace('*phone*', new_phone)

    if '#phone#' in request_data:
        phone = user_config['investor_user']['phone']
        request_data = request_data.replace('#phone#', phone)

    if '#pwd#' in request_data:
        pwd = user_config['investor_user']['pwd']
        request_data = request_data.replace('#pwd#', pwd)

    # print(request_data)
    # print(info)

    resp = requests.request(method=info['method'],
                            url=yaml_config['host'] + info['url'],
                            headers=eval(info['headers']),
                            json=eval(request_data))
    try:
        assert resp.json()['msg'] == info['expected']
    except AssertionError as e:
        logger.error(e)
        logger.info("测试数据: {}".format(request_data))
        raise e
