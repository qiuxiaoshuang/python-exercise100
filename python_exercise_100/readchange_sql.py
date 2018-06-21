# -*- coding: utf-8 -*-
# import pymysql
#
# #  获取数据库连接
# conn= pymysql.connect(
#     host='localhost',  # host主机名
#     user='root',  # user用户名
#     passwd='123456',  # passwd密码
#     db='test',  # db数据库名称
#     port=3306,  # port端口
#     charset='utf8'  # charset编码
# )
# # #打印数据库连接对象
# # print('数据库连接对象为：{}'.format(conn))
# # 获取游标
# cur = conn.cursor();




import pymysql

class MysqlClient(object):
    def __init__(self, host="localhost", user="root", passwd="123456", db="test"):
        conf = {
            "host": host,
            "user": user,
            "passwd": passwd,
            "db": db,
            "cursorclass": pymysql.cursors.DictCursor,
            "charset": "utf8"
        }
        self.conn = pymysql.connect(**conf)

    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        row = cursor.fetchall()
        return row

    def update(self, sql):
        cursor = self.conn.cursor()
        effect_row = cursor.execute(sql)
        self.conn.commit()
        return effect_row

    def insert_many(self, sql, param):
        cursor = self.conn.cursor()
        effect_row = cursor.executemany(sql, param)
        self.conn.commit()
        return effect_row

    def __del__(self):
        self.conn.close()





def get_sno_degree():
    sno_degree = {}
    mysql = MysqlClient(host="localhost", user="root", passwd="123456", db="test")
    sql = "select sno,degree from scores where cno='3-105'"
    rows = mysql.query(sql=sql)
    for row in rows:
        sno = row["sno"]
        # cno = row["cno"]
        degree = row["degree"]
        sno_degree[sno] = degree
    return sno_degree
# 输出decimal(18,0) 18是定点精度,0是小数位数。
# decimal(a,b)
# a指定指定小数点左边和右边可以存储的十进制数字的最大个数，最大精度38。
# b指定小数点右边可以存储的十进制数字的最大个数。小数位数必须是从 0 到 a之间的值。默认小数位数是 0。


def get_sname_degree():
    sname_degree = {}
    mysql= MysqlClient(host="localhost", user="root", passwd="123456", db="test")
    sql = "select sname,degree,cname from students left join  scores on students.sno= scores.sno left join courses on  " \
          "scores.cno=courses.cno ORDER BY sname "
    rows = mysql.query(sql=sql)
    for row in rows:
        sname = row["sname"]
        degree = row["degree"]
        cname = row["cname"]
        sname_degree[(sname,cname)] = degree
    return sname_degree


if __name__ == "__main__":
    print(get_sname_degree())
    # print(get_sno_degree())

