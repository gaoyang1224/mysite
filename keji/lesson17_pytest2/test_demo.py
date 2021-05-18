def test_demo():
    """当用例没有通过时，需要额外处理，日志处理。
    测试用例不通过，抛出异常。
    """
    try:
        print("try")
        assert 1 + 1 == 2
    except AssertionError as err:
        print("测试用例正在执行。")
        raise err
