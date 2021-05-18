class Dog:
    def __init__(self, color, ke):
        self.color = color
        self.ke = ke

    def run(self):
        print("正在跑")

my_dog = Dog("黑色", "狗类")
print(my_dog.color)

value = getattr(my_dog, "color")
print(value)