import pymysql
from pymysql.cursors import DictCursor


class DBHandler:
    def __init__(self,
                 host='',
                 port=3306,
                 user='',
                 password='',
                 charset='utf8',
                 # 指定数据库 可以不写
                 database='',
                 cursorclass=DictCursor
                 ):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    charset=charset,
                                    # 指定数据库 可以不写
                                    database=database,
                                    cursorclass=cursorclass)
        self.cursor = self.conn.cursor()

    def query_one(self, sql):
        """数据库查询"""
        self.conn.commit()
        # 'select * from futureloan.member where id = {} limit 10;'.format(1)'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data

    def query_all(self, sql):
        """数据库查询"""
        self.conn.commit()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def query(self, sql, one=True):
        """数据库查询"""
        self.conn.commit()
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# if __name__ == '__main__':
#     db = DBHandler()
#     data = db.query('select * from futureloan.member limit 10;', one=False)
#     print(data)
#     db.close()
