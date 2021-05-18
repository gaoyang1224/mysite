import pytest


@pytest.fixture(scope='function', autouse=True)  # module是模块，只运行1次，class是类，2个并一个运行
                                               # -- ,autouse=True这个是所有自动全使用夹具，不用传
def function_before():
    print("测试用例执行前")
    yield 'hello'
    print("测试用例执行后")