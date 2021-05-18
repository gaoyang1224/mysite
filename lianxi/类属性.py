"""类属性：所有成员具备的属性
类属性 == 类变量
"""
class Car:
    fadongji = True
    wheel = True
    materal = ["塑料","钢铁"]

print(Car.materal)

Car.wheel = False
print(Car.wheel)

my_car = Car()
my_car.materal = ["橡胶"]
print(my_car.materal)
print(Car.materal)