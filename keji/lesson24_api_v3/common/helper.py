"""帮助模块"""
import random

from faker import Faker

def generate_new_phone():
    """自动生成手机号"""

    fk = Faker(locale='zh_CN')
    phone = fk.phone_number()
    return phone

def generate_new_phone_2():
    """自动生成手机号"""
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for i in range(9):
        num = random.randint(0, 9)
        phone += str(num)
    return phone


if __name__ == '__main__':
    print(generate_new_phone())