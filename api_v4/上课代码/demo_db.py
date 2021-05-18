"""安装pymysql"""
from pprint import pprint

import pymysql
from pymysql.cursors import DictCursor

# 建立连接
conn = pymysql.connect(host='8.129.91.152',
                       port=3306,
                       user='future',
                       password='123456',
                       charset='utf8',
                       # 指定数据库 可以不写
                       database='futureloan',
                       cursorclass=DictCursor)
# 获取游标
cursor = conn.cursor()
# 通过游标执行sql语句
cursor.execute('select * from futureloan.member where id = {} limit 10;'.format(1))
# 通过游标获取结果
data = cursor.fetchone()
print(data)

# 关闭
cursor.close()
conn.close()