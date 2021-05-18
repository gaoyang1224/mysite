name = "yuwze wang"

# 字符串的变量.字符串操作
print(name.title())
print(name.lower())
print(name.upper())

# find: 查找某个子串， 如果能够找到，返回索引值
print(name.find("w"))
print(name.find("wa"))
# 找不到，wg, 找不到返回 -1， python规定的
print(name.find("wg"))

#