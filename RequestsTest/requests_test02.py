"""
    接口测试步骤
"""
import requests
from utils import pymysql_tools


# step1. 构造请求
u = "http://132.232.44.158:5000/userLogin/"
d = {"username":"test", "password":"123456", "captcha":"123456"}
r = requests.post(url=u, json=d)

# step2. 断言http响应状态码，非生即死
assert r.status_code == 200

# step3. 断言响应信息
res = r.json() # r.text转成字典，前提是服务器返回的信息必须是json格式的
assert res.get("code") == 200

# step4. 查询数据库，判断是否存在此记录（可选，登录，订单..）
# 目的：去为了判断后台代码是不是有问题
sql = "select * from tbl_user where username='test' and password='123456'"
dbinfo = {"host": "132.232.44.158","user": "vn", "password": "Langjintest!@#4##","db": "lux"}
result = pymysql_tools.query(dbinfo, sql)
assert len(result) == 1

print("登录测试用例通过！")