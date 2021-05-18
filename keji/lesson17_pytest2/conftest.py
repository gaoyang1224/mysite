import pytest


@pytest.fixture(scope='function', autouse=True)
def function_before():
    """用例前置条件"""
    print("测试用例执行前")
    yield "chrome" # 生成器函数
    print("测试用例执行之后")