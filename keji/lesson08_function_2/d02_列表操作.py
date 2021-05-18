
dalao = ["哟哟哟", "wen"]

# 调用者两个函数为什么返回 None, 因为函数定义时没有返回值，
# print(dalao.append("不变的音乐"))  # 和函数的返回值有关系
# print(dalao.remove("wen"))

# print(dalao)

b = dalao.append("不变的音乐")
print(b)

# 因为 pop 这个函数有返回值
c = dalao.pop(0)
print(c)

# 函数你调用的时候得到的值是由返回值决定的。

