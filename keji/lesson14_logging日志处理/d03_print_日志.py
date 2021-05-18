class Dog():

    def __init__(self, color):
        print("正在初始化....")
        self.color = color
        print("已经定义好了 color 属性")
        self.ke = "dog"
        print("已经定义好了 ke 属性")
        try:
            a = []
            a[100]
        except IndexError:
            print("出现了错误。。。。。。。。。。。。。。。！！！！！！")


    def run(self):
        print("狗在跑")


dog = Dog("黑色")
print("已经定义好了 color 属性")