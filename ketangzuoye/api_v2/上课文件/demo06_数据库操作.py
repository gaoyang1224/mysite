"""
mysql , oracle , sql-server , postgres , redis , mongodb
mariadb

mysql
安装
pip install pymysql
"""

import pymysql
from pymysql.cursors import DictCursor
# 建立连接


conn = pymysql.connect(host='8.129.91.152',
                       port=3306,
                       user='future',
                       password='123456',
                       # 不要写成utf-8
                       charset='utf8',
                       database='futureloan',
                       cursorclass=DictCursor
                       )
# 获取游标
cursor = conn.cursor()
# 通过游标执行sql语句
cursor.execute('select * from futureloan.member limit 10;')
# 通过游标得到结果
# data = cursor.fetchall()
data = cursor.fetchone()

# 查一行
print(data)

# 关闭
cursor.close()
conn.close()
