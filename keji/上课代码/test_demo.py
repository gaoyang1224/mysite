import pytest

@pytest.fixture(autouse=True)
def connect():
    print("链接")
    return "大脸猫"


def test_demo():
    print("helloworkd")
    # print(connect)
    assert 1 == 1