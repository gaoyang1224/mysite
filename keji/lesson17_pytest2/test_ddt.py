"""
写一个登陆函数，输入用户名和密码，如果用户名='yuz' 并且 密码 = ‘123456’ 返回 ”登陆成功“， 否则返回”登陆失败“
编写测试用例函数，测试上面的登陆函数。至少 3 个测试用例。
使用 pytest 运行登陆成功用例。 （可以把运行的命令作为注释写在模块中）。
"""
import pytest


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
def test_login(info):
    # test_login_1
    # test_login_2
    # test_login_3
    u = info['username']
    p = info['password']
    exp = info['expected']
    assert exp == login(u, p)
