"""
什么是函数
f(x) = x + 1   ， x = 4
y = x + 2

python 当中的函数和数学函数并没有本质的区别。
就是从数学函数。

# 函数的定义
def 函数名():
    # 函数体
    return 函数的返回值

函数定义好了以后并不会执行函数体，
如果要执行函数体，需要调用函数。

函数调用之前必须要定义，先定义再调用。
再函数定义的时候，最好不要调用它自己


函数作用: 把一段可以重复运行的代码（3行，100行）放到函数体当中。
去调用函数的时候，

什么时候想到用函数：你有很多功能相同的代码需要多次运行。。。 你再复制粘贴一段代码的时候。
"""

# print("before")

def print_all_dalao():
    """打印所有的大佬。 Docstring 文档字符串， 说明函数的作用"""
    # 函数体：运行函数的时候会执行的代码
    print("1级大佬旧梦")
    print("2级大佬阿鸡")
    print("3级大佬Niki")

    # 调用的时候
    # print_all_dalao()


# print("hello")
# # print_all_dalao()
# print("other")


print("1级大佬旧梦")
print("2级大佬阿鸡")
print("3级大佬Niki")

print("1级大佬旧梦")
print("2级大佬阿鸡")
print("3级大佬Niki")


print("1级大佬旧梦")
print("2级大佬阿鸡")
print("3级大佬Niki")

print("1级大佬旧梦")
print("2级大佬阿鸡")
print("3级大佬Niki")

print("1级大佬旧梦")
print("2级大佬阿鸡")
print("3级大佬Niki")

print("1级大佬旧梦")
print("2级大佬阿鸡")
print("3级大佬Niki")

print("1级大佬旧梦")
print("2级大佬阿鸡")
print("3级大佬Niki")


# 调用5次
print_all_dalao()
print_all_dalao()
print_all_dalao()
print_all_dalao()
print_all_dalao()


