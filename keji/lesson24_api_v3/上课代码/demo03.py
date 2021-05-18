"""类和对象"""

class A:
    def __init__(self, param1, param2):
        pass

    def run(self):
        pass

class B(A):
    def run_abc(self):
        pass


# 怎么得到对象：实例化
a = A('a' , 'b')
a.run()

b = A()

