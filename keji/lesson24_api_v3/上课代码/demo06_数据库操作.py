"""
mysql, oralce, sql-server, postgres, redis, mongodb
mariadb

mysql.
安装：
pip install pymysql

"""
import pymysql

# 1.建立链接
conn = pymysql.connect(host='8.129.91.152',
                       port=3306,
                       user='future',
                       password='123456',
                       # 不要写成utf-8
                       charset='utf8',
                       # 指定数据库
                       database='futureloan'
                       )
# 2.获取游标
cursor = conn.cursor()
# 3.通过游标执行sql语句
cursor.execute('SELECT * FROM futureloan.member WHERE id={} LIMIT 10;'.format(1))

# 4.通过游标得到结果
# data = cursor.fetchall()
# print(data)
data = cursor.fetchone()
print(data)

# 数据库，请用类封装
