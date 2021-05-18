import pytest





def login(username, password):
    if username == 'gaoyang' and password == '123456':
        return '登录成功'
    return '登录失败'


data = [
    {"username": "gaoyang", "password": "123456", "expected": "登录成功"},
    {"username": "", "password": "", "expected": "登录失败"},
    {"username": "g", "password": "1", "expected": "登录失败"}
]


@pytest.mark.parametrize('test_info', data)
def test_login(test_info, function_before):
    u = test_info['username']
    p = test_info['password']
    exp = test_info['expected']
    assert exp == login(u, p)


class Testuser:
    def test_user_1(self, function_before):
        pass

    def test_user_2(self, function_before):
        pass
