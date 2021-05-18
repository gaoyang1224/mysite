class Animal:
    def __init__(self, ke, color):
        self.ke = ke
        self.color = color

    def run(self):
        print("正在跑")

    def eat(self):
        print("正在吃饭")


class Dog(Animal):
    def __init__(self, color, kind):
        super().__init__("dog", color)
        self.kind = kind


    def run(self):
        super().run()
        print("正在散步")


# my_dog = Dog()
# my_dog.run()

animal = Animal("狗科", "黑色")
dog = Dog("黑色", "金毛")
print(dog)
print(dog.ke)
print(dog.kind)
