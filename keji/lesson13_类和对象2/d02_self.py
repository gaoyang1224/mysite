"""
self 在类定义里面表示对象本省，可以修改成其他的变量，但是不要改。
规范。

实例属性的定义 self.属性

"""

class Car:
    fadongji = True
    wheel = True
    material = ["塑料", "橡胶"]

    def __init__(self, logo, color):
        print("对象产生时进行的初始化工作")
        print("类里面的", id(self))
        self.brand = logo  # brand 属性设置成 logo
        self.color = color


my_car = Car("丰田", "紫色")
fengtian_car = my_car
print("类外面", id(my_car))