"""
实例属性：个体具备的特征
__init__()
"""
class Car:
    fadongji = True
    wheel = True
    materal = ["塑料","钢铁"]

    def __init__(self,logo,color):
        """初始化函数"""
        self.brand = logo          # self.brand是实例， logo和color是参数
        self.color = color


my_car = Car("Tesla","red")
print(my_car)
print(my_car.brand)


my_car.brand = "本田"
print(my_car.brand)