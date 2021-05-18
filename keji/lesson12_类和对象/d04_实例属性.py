"""
实例属性：个体（对象）具备的特征， 这些特征可以一样，也可以不一样。

__init__() 方法：
类下面的函数就叫方法
不能有返回值

self, 在类定义过程中，类的里面代表一个实例。
"""


class Car:
    fadongji = True
    wheel = True
    material = ["塑料", "橡胶"]

    def __init__(self, logo, color):
        """初始化方法，初始化函数。"""
        print("对象产生时进行的初始化工作")
        print("类里面的", id(self))
        self.brand = logo  # brand 属性设置成 logo
        self.color = color


# 当__init__ 有参数的时候，
my_car = Car("Tesla", "red")
your_car = Car("丰田", "yes")

print(my_car)
print("累外面", id(my_car))
print(my_car.brand)

# 修改实例属性
my_car.brand = "本田"
print(my_car.brand)

# 类能不能修改实例属性

Car.brand = "莲花"
print(Car.brand)
print(my_car.brand)


