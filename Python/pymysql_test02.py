"""
    从外部py文件来引用pymysql查询/修改/删除/增加方法
"""
# 1. 导入01， 给01起一个名字：dbtools
import pymysql_test01 as dbtools

# 在外部来commit方法
sql = "insert into tbl_testcase values(null, 'https://www.zhihu.com/', 'user=ljtest', '200')"
result = dbtools.commit(dbtools.dbinfo, sql)
print(result)

# 在外部引用查询
sql = "select * from tbl_testcase"
resuts = dbtools.query(dbtools.dbinfo, sql)                 # dbtools.query:去引用01的query方法，dbtools.dbinfo：去引用01的dbinfo
for i in resuts:
    print(i)
