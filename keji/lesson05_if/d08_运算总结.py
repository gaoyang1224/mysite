# 比较， 成员， 逻辑运算

print(not None) # NoneType True


# 当你进行逻辑运算时，不为 0 的代表 True, 0 代表 False
# 字符串： 空字符 ==》 False, 否则就时 True
# 表示空，0， False,
print(not 1)  # False
print(not 0) # True
print(not -1) # False

print(not "abc")
print(not " ")
print(not "")

print(not ["b"])
print(not [])

print(not {})


# 不是返回布尔类型
# 自己去试
print(9 and 2)