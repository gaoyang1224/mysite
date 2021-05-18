import logging


def add(a, b):
    return a+b

def test_add():
    ret = add(3, 4)
    expected = 8
    # if ret == expected:
    #     print("测试通过")
    # else:
    #     print("测试不通过")
    # try:
    #     assert expected == ret
    # except AssertionError as e:
    #     logging.error("断言失败:", e)
    assert expected == ret


def test_minus():
    assert 7 == add(3 - 4)




if __name__ == '__main__':
    test_add()
    test_minus()