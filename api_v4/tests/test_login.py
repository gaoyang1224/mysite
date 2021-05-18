import json

import pytest
import requests
from middleware.handler import GYHandler


data = GYHandler.excel.read('login')

@pytest.mark.parametrize('info', data)
def test_login(info):
    request_data = info['json']
    if '*phone*' in request_data:
        new_phone = GYHandler.generate_new_phone()
        request_data = request_data.replace('*phone*', new_phone)

    if '#phone#' in request_data:
        phone = GYHandler.user_config['investor_user']['phone']
        request_data = request_data.replace('#phone#', phone)

    if '#pwd#' in request_data:
        pwd = GYHandler.user_config['investor_user']['pwd']
        request_data = request_data.replace('#pwd#', pwd)

    print(request_data)

    resp = requests.request(method=info['method'],
                            url=GYHandler.yaml_config["host"] + info['url'],
                            headers=json.loads(info['headers']),
                            json=json.loads(request_data))

    try:
        assert resp.json()['msg'] == info['expected']
    except AssertionError as e:
        GYHandler.logger.error(e)
        return e
