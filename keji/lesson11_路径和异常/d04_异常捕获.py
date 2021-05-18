"""
捕获：防止程序中断，正常执行
except: 出现异常以后会执行的代码
try:
    a / b
except:
    pass

当进行异常捕获
"""
a = 3
b = 1

try:
    a / b
except:
    print("b 不能为 0")

print("无论如何都会执行")