"""
在一个函数当中，能不能调用本身。

可以调用其他函数吗

我先找一下这个文件当中有哪些函数，顶格写的。

"""


def get_offer(name, money, food):
    """获取 offer"""
    print("{} 拿到了 一个 {}k 的 offer".format(name, money))
    eat(name, food)


get_offer("旧梦", 23, "龙虾")


def eat(eat_name, eat_food):
    print("{} 最喜欢吃 {}".format(eat_name, eat_food))

# name = "旧梦"
# eat_name = name
# eat_name = name = "旧梦"

# name = "旧梦"
# name = name


## 函数的作用域
## 内置函数
## open() 内置函数。文件操作。