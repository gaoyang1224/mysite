"""
fixture,测试夹具。 测试用例执行的前置动作和后置动作。
前置条件：

"""
import pytest

# 夹具：函数



def login(username, password):
    """开发写的功能"""
    if username == 'yuz' and password == '123456':
        return "登陆成功"
    return "登陆失败"


data = [
    {"username": "yuz", "password": "123456", "expected": "登陆成功"},
    {"username": "", "password": "", "expected": "登陆失败"},
    {"username": "a", "password": "b", "expected": "登陆失败"},
]


@pytest.mark.parametrize('info', data)
def test_login(info, function_before):
    u = info['username']
    p = info['password']
    exp = info['expected']
    assert exp == login(u, p)

def test_demo(function_before):
    # 使用夹具名称可以直接获取返回值。
    print(function_before)
    assert 1 + 1 == 3

class TestUser:
    def test_user_1(self):
        pass

    def test_user_2(self):
        pass

