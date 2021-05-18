"""
except 异常类型：捕获指定类型的异常


"""

a = 3
b = 0

try:
    # 可能发生异常的代码
    lst = [1,2]
    lst[100]
    # [1,2][100]
    a / b
except ZeroDivisionError as err:
    print(err)
    print("记录")
except IndexError as err:
    print(err)
    print("赶紧联系开发。")

print("无论如何都会执行")