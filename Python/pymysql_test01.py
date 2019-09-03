"""
    PyMysql工具箱，python连接并操作mysql数据用的
"""
# 1.导入pymysql包
import pymysql

# 把mysql、数据库相关信息写好
dbinfo = {
    "host": "127.0.0.1",    # mysql主机ip或域名
    "user": "root",         # mysql用户名         
    "password": "123456",   # mysql密码
    "db": "ljtest"          # 要连接的数据库
}

# 2. 定义一个叫query的方法，是为了当我们调用这个方法时候，
# 传入对应的参数，就可以从数据库里面查询到信息
def query(dbinfo, sql):
    """
        pymysql查询mysql数据库
        返回值：
            成功： 返回结果
            失败： 返回None
    """
    db = pymysql.connect(**dbinfo)                  # 4. 去连接mysql，并且打开对应的表
    cursor = db.cursor()                            # 5. 获取游标，查询敞口
    try:                                            # 6. 通过使用游标来执行sql的查询操作
        cursor.execute(sql)                         # 执行sql语句
        res = cursor.fetchall()                     # # 7. 获取查询的结果
        db.close()                                  # 关闭数据连接
        return res
    except:
        return None


def commit(dbinfo, sql):
    """
        mysql数据的增加/删除/修改
        返回值：
            成功： 返回True
            失败： 返回False
    """
    db = pymysql.connect(**dbinfo)          # 连接数据库
    cursor = db.cursor()                    # 获取游标
    try:
        cursor.execute(sql)                 # 执行sql语句
        db.commit()                         # 执行sql之后，必须要去commit一下
        db.close()                          # 关闭数据库连接
        return True
    except:
        return False

if __name__ == "__main__":
    """
        只有在py模块里面运行的时候，才会执行下面的代码；
        从外部导入pymysql_test01.py，则不会不会运行下面的代码。
    """
    # 查询用法
    # sql = 'select * from tbl_testcase where url like "%google%"'
    # a = query(dbinfo, sql)
    # print(a)

    # 增加
    # sql = "insert into tbl_testcase values(null, 'https://www.zhihu.com/', 'user=ljtest', '200')"
    # a = commit(dbinfo, sql)
    # print(a)

    # 删除的用法
    # sql = "delete from tbl_testcase where url like '%google%'"
    # a = commit(dbinfo, sql)
    # print(a)

    # 修改的用法
    sql = "update tbl_testcase set params = '{}' where id = 7".format('password="123"')
    a = commit(dbinfo, sql)
    print(a)
