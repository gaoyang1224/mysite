"""充值接口测试"""

import pytest
import os
import json

import requests

from common.logger_handler import logger
from config import path
from common.excel_handler import ExcelHandler
from common.yaml_handler import yaml_config, user_config
from common.helper import generate_new_phone

excel_file = os.path.join(path.data_path, 'cases.xlsx')
data = ExcelHandler(excel_file).read('recharge')


@pytest.mark.parametrize('info', data)
def test_recharge(info, login):
    """充值"""
    # 先要替换
    if "#member_id#" in info['data']:
        info["data"] = info["data"].replace('#member_id#', str(login['id']))

    # token 组装方式 1：通过excel 替换
    # if "#token#" in info['headers']:
    #     info["headers"] = info["headers"].replace('#token#', login['token'])

    # token 组装2： 通过 headers 添加
    headers = json.loads(info["headers"])
    headers['Authorization'] = login['token']

    if "*wrong_member_id*" in info['data']:
        info["data"] = info["data"].replace('*wrong_member_id*', str(login['id'] + 1))

    resp = requests.request(url=yaml_config['host'] + info['url'],
                     method=info['method'],
                     headers=headers,
                     json=json.loads(info['data']))
    assert resp.json()['code'] == info['expected']
