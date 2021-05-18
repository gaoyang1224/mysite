"""充值接口"""
import json
import pytest
import requests
from decimal import Decimal
from middleware.handler import GYHandler


data = GYHandler.excel.read('recharge')


@pytest.mark.parametrize('info', data)
def test_recharge(info, login, db):
    if "#member_id#" in info['data']:
        info['data'] = info['data'].replace("#member_id#", str(login['id']))

    if "token#" in info['headers']:
        info['headers'] = info['headers'].replace("#token#", login['token'])

    if "*wrong_member_id*" in info['data']:
        info['data'] = info['data'].replace("*wrong_member_id*", str(login['id'] + 1))

    # token 另一种方法
    # headers = json.loads(info['headers'])
    # headers['Authorization'] = login['token']

    # 访问数据库，充值之前的余额
    sql = 'select leave_amount from member where id ={}'.format(login['id'])
    result = db.query(sql)
    money_before = result['leave_amount']

    data = json.loads(info['data'])
    resp = requests.request(method=info['method'],
                            url=GYHandler.yaml_config["host"] + info['url'],
                            headers=json.loads(info['headers']),
                            json=data)
    assert resp.json()['code'] == info['expected']

    if resp.json()['code'] == 0:
        sql = 'select leave_amount from member where id ={}'.format(login['id'])
        result = db.query(sql)
        momey_after = result['leave_amount']
        momey = Decimal(str(data['amount']))
        assert money_before + momey == momey_after
