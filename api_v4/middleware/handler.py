from faker import Faker
from pymysql.cursors import DictCursor

from common.db_handler import DBHandler
from common.logger_handler import get_logger
from common.yaml_handler import read_yaml
import os
from config import path
from common.excel_handler import ExcelHandler


class MidDBHandler(DBHandler):
    def __init__(self):
        yaml_path = os.path.join(path.config_path, 'config.yaml')
        yaml_config = read_yaml(yaml_path)

        user_path = os.path.join(path.config_path, 'security.yaml')
        user_config = read_yaml(user_path)

        super().__init__(host=user_config['db']['host'],
                         port=user_config['db']['port'],
                         user=user_config['db']['user'],
                         password=user_config['db']['password'],
                         charset='utf8',
                         # 指定数据库 可以不写
                         database=user_config['db']['database'],
                         cursorclass=DictCursor)


class GYHandler():
    """任务：中间层   common和调用层"""
    yaml_path = os.path.join(path.config_path, 'config.yaml')
    yaml_config = read_yaml(yaml_path)

    user_path = os.path.join(path.config_path, 'security.yaml')
    user_config = read_yaml(user_path)

    # logger
    logger_file = os.path.join(path.logs_path, yaml_config['logger']['file'])
    logger = get_logger(name=yaml_config['logger']['name'],
                        file=logger_file)

    # excel
    excel_file = os.path.join(path.data_path, 'cases.xlsx')
    excel = ExcelHandler(excel_file)

    # 数据库
    db_class = MidDBHandler

    @staticmethod
    def generate_new_phone():
        """自动生成手机号码"""
        fk = Faker(locale="zh_CN")
        while True:
            phone = fk.phone_number()
            db = MidDBHandler()
            phone_in_db = db.query('select * from member where mobile_phone= {}'.format(phone))
            db.close()
            if not phone_in_db:
                return phone
