# or and not
# and 并且，、
# or , 或者
data = 5 > 3
print(data)

door = 4 == 3
print(door)

# and, 左边和右边必须同时为真，True, 才能为真， 否则就是False
print(data and door)

# or 只要一个为真， 就是真爱。
print(data or door)

# not 反面：杠精
print(not door)

# 多个运算， 先算哪一个。 运算的优先级
# () 提高运算优先级
print( (5 > 6) and (7 < 3) or ("yuz" == "旧梦"))
