"""
包含：Animal 包含狗类
狗类 叫做  Animal 类的子类
Animal 是父类

继承：他就可以使用父类的所有属性和方法。

当父和子具有相同的方法，属性。 如果自己有，先调用自己。

方法重写。

多重继承
"""

class Animal:
    def run(self):
        print("动物正在跑。。。。")


class Dog(Animal):
    def run(self):
        print("狗在跑")

class NotClever:
    def chaijia(self):
        print("拆家")

class Erha(Dog, NotClever):
    pass


dog = Dog()
dog.run()

erha = Erha()
erha.run()
erha.chaijia()

# 获取继承的优先调用顺序
print(Erha.__mro__)

