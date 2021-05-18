def eating(name, sexy, age):
    print('{} 正在吃狗粮，他的性别是 {}, 年龄是 {}'.format(name, sexy, age))


def bark(name, sexy, age):
    print('{} 正在叫，显然是饿了。他的性别是 {}, 年龄是 {}'.format(name, sexy, age))


def bath(name, sexy, age):
    print('{} 正在洗澡。他的性别是 {}, 年龄是 {}'.format(name, sexy, age))

name = "single dog"
sexy = "男"
age = 17

# eating(name, sexy, age)
# bark(name, sexy, age)
# bath(name, sexy, age)


name = "single dog"
sexy = "男"
age = 17

class Dog:
    #name = "single dog"
    # sexy = "男"
    # age = 17

    def __init__(self, name, sexy, age):
        self.name = name
        self.gender = sexy
        self.age = age

    def eating(self, food):
        # 吃什么东西
        print('{} 正在吃狗粮，他的性别是 {}, 年龄是 {}'.format(
            self.name,
            self.gender,
            self.age))

    def bark(self):
        print('{} 正在叫，显然是饿了。他的性别是 {}, 年龄是 {}'.format(
            self.name,
            self.gender,
            self.age))

    def bath(self):
        print('{} 正在洗澡。他的性别是 {}, 年龄是 {}'.format(
            self.name,
            self.gender,
            self.age))


single_dog = Dog(name, sexy, age)
single_dog.eating()
single_dog.bark()
single_dog.bath()

# 类和对象可以帮我们存储各个不同的函数需要用到的共同变量
