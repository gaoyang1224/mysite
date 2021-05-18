import pytest
import requests

from common.db_handler import DBHandler
from common.yaml_handler import yaml_config, user_config
from jsonpath import jsonpath

from middleware.handler import YZHandler


@pytest.fixture()
def login():
    """登录。 得到 ID, token, leave_amount
    """
    user = {
        "mobile_phone": user_config['investor_user']['phone'],
        "pwd": user_config['investor_user']['pwd']
    }
    resp = requests.request(method='POST',
                    url=yaml_config['host'] + '/member/login',
                    headers={"X-Lemonban-Media-Type": "lemonban.v2"},
                    json= user
                     )
    resp_json = resp.json()

    # token = resp_json["data"]["token_info"]["token"]
    # token_type = resp_json["data"]["token_info"]["token_type"]

    token = jsonpath(resp_json, '$..token')[0]
    token_type = jsonpath(resp_json, '$..token_type')[0]
    id = jsonpath(resp_json, '$..id')[0]
    leave_amount = jsonpath(resp_json, '$..leave_amount')[0]

    token = " ".join([token_type, token])
    return {"id": id,
            "token": token,
            "leave_amount": leave_amount}

@pytest.fixture()
def db():
    """管理数据库链接的夹具"""
    db_conn = YZHandler.db_class()
    yield db_conn
    db_conn.close()

if __name__ == '__main__':
    print(login())