# -*- coding: utf-8 -*-
# import pymysql
#
# try:
#     #  获取数据库连接
#     conn= pymysql.connect(
#         host='localhost',  # host主机名
#         user='root',  # user用户名
#         passwd='root',  # passwd密码
#         db='test',  # db数据库名称
#         port='3306',  # port端口
#         charset='utf8'  # charset编码
#     )
# #打印数据库连接对象
#     print('数据库连接对象为：{}'.format(conn))
#     # 获取游标
#     cur = conn.cursor()

# -*- coding: utf-8 -*-











def get_name_degree():
    name_degree = {}
    mysql = MysqlClient(host="localhost", user="root", passwd="root", db="test")
    sql = "select sname, degree from students left join  scores where students.sno= scores.sno"
    rows = mysql.query(sql=sql)
    for row in rows:
        sname = row["sname"]
        degree = row["degree"]
    return name_degree

if __name__ == "__main__":
    print(get_name_degree())

