# 变量，局部变量和全局变量
# 局部：在函数体或者代码块里面定义的变量
# 全局：文件里面定格定义的变量

# 局部作用域能不能获取全局变量
# 全局作用域能不能获取局部变量

# 局部作用域能不能修改全局变量
# 全局作用域能不能修改局部变量



# def add(a, b):
#     c = a + b
#     return c + 2
#
# a = 2
# # a = 4
# b = 3
# print(add(a, b))

# # 局部作用域能不能获取全局变量 可以
# a = "随风"
# def add():
#     b = a + "王"
#     print(b)
#     return None
# add()


# 全局作用域能不能获取局部变量
# return
# def add():
#     a = 1
#     print(a)
#     return a
#
# # print(a)
# print(add())


# # 局部作用域能不能修改全局变量 可以
a = "随风"
def add():
    # 把 a 当成了局部变量
    # a = "王"
    global a
    a = a + "王"
    print(a)
    return None

add()
