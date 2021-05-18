"""帮助模块"""
from faker import Faker

from common.db_headler import DBHandler


def generate_new_phone():
    """自动生成手机号码"""
    fk = Faker(locale='zh_CN')
    while True:
        phone = fk.phone_number()
        db = DBHandler()
        phone_in_db = db.query('select * from member where mobile_phone={}'.format(phone))
        # 查询数据库
        # 如果数据库里有这条记录，重新生成新的手机号
        db.close()
        if not phone_in_db:
            return phone


if __name__ == '__main__':
    print(generate_new_phone())
