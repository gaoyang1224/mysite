import pytest
import requests
from jsonpath import jsonpath
from middleware.handler import GYHandler
from common.db_handler import DBHandler


@pytest.fixture()
def login():
    user = {
        "mobile_phone": GYHandler.user_config['investor_user']['phone'],
        "pwd": GYHandler.user_config['investor_user']['pwd']
    }
    resp = requests.request(method='post',
                            url=GYHandler.yaml_config['host'] + '/member/login',
                            headers={"X-Lemonban-Media-Type": "lemonban.v2"},
                            json=user)
    resp_json = resp.json()

    token = jsonpath(resp_json, '$..token')[0]
    token_type = jsonpath(resp_json, '$..token_type')[0]
    token = " ".join([token_type, token])
    id = jsonpath(resp_json, '$..id')[0]
    leave_amount = jsonpath(resp_json, '$..leave_amount')[0]

    # token = resp_json['data']['token_info']['token']
    # token_type = resp_json['data']['token_info']['token_type']
    # id = resp_json['data']['id']
    # leave_amount = resp_json['data']['leave_amount']
    # return token, id, leave_amount
    return {
        "id": id,
        "token": token,
        "leave_amount": leave_amount}


@pytest.fixture()
def db():
    """管理数据库连接"""
    db_conn = GYHandler.db_class
    yield db_conn
    db_conn.close()



if __name__ == '__main__':
    print(login())
