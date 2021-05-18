class Dog:
    def __init__(self, name, sexy, age):
        self.name = name
        self.sexy = sexy
        self.age = age

    def jiao(self,sanbu):
        print('{}在叫，他的性别是{}，他的年龄是{},爱{}'.format(self.name,
                                                        self.sexy,
                                                        self.age,
                                                        sanbu))


    def bake(self):
        print('{}在叫，他的性别是{}，他的年龄是{}'.format(self.name,
                                                        self.sexy,
                                                        self.age))

    def eating(self):
        print('{}在叫，他的性别是{}，他的年龄是{}'.format(self.name,
                                                        self.sexy,
                                                        self.age))


name = "gougou"
sexy = "男"
age = 18
sanbu = "散步"

my_dog = Dog(name, sexy, age)
my_dog.jiao(sanbu)

