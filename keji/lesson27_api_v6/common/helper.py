"""帮助模块"""
import random

from faker import Faker

from common.db_handler import DBHandler


def generate_new_phone():
    """自动生成手机号"""
    fk = Faker(locale='zh_CN')
    while True:
        phone = fk.phone_number()
        db = DBHandler()
        phone_in_db = db.query('SELECT * FROM member WHERE mobile_phone = {}'.format(phone))
        db.close()
        if not phone_in_db:
            return phone
        # 查询数据库
        # 如果数据库里有这条记录，重新生成新的手机号码


def generate_new_phone_2():
    """自动生成手机号"""
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for i in range(9):
        num = random.randint(0, 9)
        phone += str(num)
    return phone


if __name__ == '__main__':
    print(generate_new_phone())