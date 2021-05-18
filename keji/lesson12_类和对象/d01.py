"""分组捕获。
异常也可以分组。

"""

try:
    # 可能发生异常的代码
    lst = [1,2]
    lst[100]
    # [1,2][100]
    a / b
except (ZeroDivisionError, IndexError) as err:
    print(err)
    print("记录")
except (KeyError, ValueError) as e:
    print("赶紧联系开发")
# except IndexError as err:
#     print(err)
#     print("赶紧联系开发。")
finally:
    # 无论如何都会执行，不管有没有捕获到 except
    # 文件，关闭
    print("无论如何都会执行的操作")

with open("file") as f:
    pass


# try:
#     f = open()
# except:
#     错误逻辑
# finally:
#     f.close()


try:
    pass
except:
    pass
else:
    # 当 except 没有被触发的时候
    # 会执行的代码
    pass