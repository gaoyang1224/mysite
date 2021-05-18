# 同时对多个数据进行判断
# while , for

#
say_sth = "我喜欢你"

times = 0

# if times > 999:
#     print("接受")
# else:
#     print("不接受")
#
# times += 1
#
# if times > 999:
#     print("接受")
# else:
#     print("不接受")
# times += 1
#
# if times > 999:
#     print("接受")
# else:
#     print("不接受")
# times += 1
#
# print(times)

# while
"""
while 条件表达式：
    符合条件需要运行的代码
    通常会有变量值的改变

条件表达式不满足的情况退出来
"""

say_sth = "我喜欢你"
times = 0
while times <= 999:
    times += 1
    print(say_sth)
    print("不接受")
    print("我已经尝试了{} 次".format(times))


print("next")
print(times)





