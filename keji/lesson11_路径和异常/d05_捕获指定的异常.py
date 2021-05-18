"""
except 异常类型：捕获指定类型的异常


"""

a = 3
b = 0

try:
    a / b
except Exception as err:
    print(err)
    print("b 不能为 0")

print("无论如何都会执行")