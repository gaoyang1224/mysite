"""super函数

子类的方法想调用父类的方法。 超继承
"""

class Animal:

    def __init__(self, ke, color):
        self.ke = ke
        self.color = color

    def run(self):
        print("动物正在跑。。。。")

    def eating(self):
        print("正在吃食物。")


class Dog(Animal):
    def __init__(self, dog_color, kind):
        # 调用父类的初始化函数，然后再定义自己的特征。
        # self.color = color
        # Animal()
        #
        super().__init__("dog", dog_color)
        self.kind = kind

    def run(self):
        # a = Animal()
        # a.run()
        # super().run()
        print("狗在跑")
        super().eating()



# my_dog = Dog()
# my_dog.run()

# 初始化 animal
animal = Animal("dog", "black")

# 初始化 dog
# dog = Dog("dog", "black")
dog = Dog("black")
print(dog)
print(dog.ke)