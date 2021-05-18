# 无序和有序
# 字典是无序的
# 列表，元组，字符串都是有序

# 能用索引获取的有序的
# 不能用索引的无序的， key


# 可变和不可变

# 可变：列表， 字典， 改变里面的 "元素"
# 不可变：字符串，元组，：   不可以修改里面的 ”元素“

# a = [1,2,("hello", "world")]
# a[2] = "orange"
# print(a)
#
# print(a[2][0])
# # NO
# a[2][0] = "love"


b = (["hello", "world"], ("ming", "ming"))
print(b[0])
# b[0] = True  # NO
# print(b)
#
# b[1] = False  # No

# b[0][0] = True # Yes
# print(b)

# b[1][0] = False
# print(b)

