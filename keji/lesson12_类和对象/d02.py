"""
什么是类和对象？
难度：5星级

什么是类？（人以群分，物以类聚）
- 人类
- 禽类
- 兽类
- 鸟类
英文： class

因为某些个体之间具备了相同的特征和行为，称为一个类

高富帅类：
    身高 > 180
    身价 > 2000 万
    颜值 ： 高

首富：
    max(身价)

命名：
    class a:
    一般驼峰命名

对象（Object), 实例

# 内存地址相同，表示的是同一个对象，数据。
可以通过 id(obj) 函数获取

"""
# 第一种
class Car:
    pass
# 第二种
# class Car():
#     pass
# # 第三种
# class Car(object):
#     pass

my_car = Car() # 实例化
# 先有类才有对象
your_car = Car()
suifeng_car = Car()

# <__main__.Car object at 0x00000246FF361608>
print(my_car)
print(id(my_car))
print(your_car)
print(suifeng_car)

# 对象的比较
a = Car()
b = Car()
print(a == b)
print(Car() == Car())  # False

# 类和对象
print(Car)
print(Car())
print(Car == Car())  # False
print(Car == Car)  # True







