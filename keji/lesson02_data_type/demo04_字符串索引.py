## 索引 index, 目录， 通过一定的顺序更快捷的找到字符串当中的某个字符。
# abc

# 公式： 字符串[索引]
# TODO: python获取索引是从 0 开始的，不是 1
name = "yuze wang"
print(name[1])
print(name[0])
# 获取空格
print(name[4])

name = """wang
yong
"""
print(name[5])


print("yuz"[1])

# 索引能不能是负数, 是从右边开始数
name = "yuz wang"
print(name[-2])
print(name[0])

# 索引超出范围了怎么办？？？
# IndexError: string index out of range
# print(name[100])


# 获取字符串的长度
print(len(name))

name = "hello,'yuz'"
print(name)

