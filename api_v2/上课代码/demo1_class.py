class Dog:
    def __init__(self, jiao):
        self.jiao = jiao

    def white_Dog(self, white):
        ws = self.jiao
        wa = ws[white]
        return wa

if __name__ == '__main__':
    a = Dog('aaa')
    b = a.white_Dog('bai')
    print(b)

