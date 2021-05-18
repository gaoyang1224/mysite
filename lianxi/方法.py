class Car:
    fadongji = True
    wheel = True
    materal = ["塑料","钢铁"]

    def __init__(self,logo,color):
        """初始化函数"""
        self.brand = logo          # self.brand是实例， logo和color是参数
        self.color = color

    def driver(self,distance=500):
        print("{}开车快,能跑{}公里".format(self,distance))


    @classmethod   #  类方法
    def fly(cls):
        print("{}正在飞".format(cls))
 
my_car = Car('h', '黑色')
my_car.driver()

# 实例方法
my_car.fly()

