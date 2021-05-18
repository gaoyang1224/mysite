"""
mysql, oralce, sql-server, postgres, redis, mongodb
mariadb

mysql.
安装：
pip install pymysql

"""
import pymysql

# 1.建立链接
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='8.129.91.152',
                       port=3306,
                       user='future',
                       password='123456',
                       # 不要写成utf-8
                       charset='utf8',
                       # 指定数据库
                       database='futureloan',
                       cursorclass = DictCursor
                       )
# 2.获取游标
cursor = conn.cursor()



# 3.通过游标执行sql语句
cursor.execute('SELECT * FROM futureloan.member LIMIT 10;')

# 4.通过游标得到结果
# data = cursor.fetchall()
# print(data)
data = cursor.fetchone()


# data_all = cursor.fetchall()

print(data)
# print(len(data_all))

# 关闭
cursor.close()
conn.close()
