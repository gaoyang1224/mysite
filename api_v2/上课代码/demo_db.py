"""安装pymysql"""
from pprint import pprint

import pymysql

# 建立连接
conn = pymysql.connect(host='8.129.91.152',
                       port=3306,
                       user='future',
                       password='123456',
                       charset='utf8')
# 获取游标
cursor = conn.cursor()
# 通过游标执行sql语句
cursor.execute('select * from futureloan.member limit 10')
# 通过游标获取结果
data = cursor.fetchone()
print(data)