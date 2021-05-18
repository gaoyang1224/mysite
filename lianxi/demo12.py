import logging

class Dog:
    def __init__(self, color, ke):
        logging.info("正在初始化")
        self.color = color
        logging.info("获取color属性")
        self.ke = ke
        try:
            a = []
            a[100]
        except IndexError:
            logging.error("有报错")

    def run(self):
        print("正在跑")

my_dog = Dog("黑色", "狗类")
print(my_dog.color)
