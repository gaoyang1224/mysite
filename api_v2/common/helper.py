"""帮助模块"""
from faker import Faker


def generate_new_phone():
    """自动生成手机号码"""
    fk = Faker(locale="zh_CN")
    return fk.phone_number()

def generate_address():
    """自动生成地址"""
    fk = Faker(locale="zh_CN")
    return fk.address()


if __name__ == '__main__':
    print(generate_new_phone())
    print(generate_address())

