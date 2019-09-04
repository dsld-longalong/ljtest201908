
import requests
from utils import excel_tools
from utils import pymysql_tools as dbtools

# 1. 取每一条测试用例， 循环执行测试用例

testcases = excel_tools.read_excel("testcase/接口测试用例模板.xlsx", "Sheet1")
for testcase in testcases:
    # 1.1 构造请求
    # 1.1.1 取出信息
    url = testcase[1]           # 用例的url
    method = testcase[5]        # 用例的方法
    datas = eval(testcase[7])   # 用例的数据，把参数字符串转换成字典
    casename = testcase[3]      # 用例名称
    http_code = int(testcase[8])# http响应状态码
    result_code = int(testcase[9]) # 接口响应的code值
    sql = testcase[10]          # 查询数据库的sql语句

    try:
        # 底层原生封装的二次方法
        res = requests.request(method=method, url=url, json=datas)
        # 1.2 断言http响应状态码
        assert res.status_code == http_code
        # 1.3 断言code
        assert res.json().get("code") == result_code
        # 1.4 断言数据库
        dbinfo = {"host": "132.232.44.158","user": "vn", "password": "Langjintest!@#4##","db": "lux"}
        r = dbtools.query(dbinfo, sql)
        assert len(r) == 1
        print("测试用例【{}】就执行成功了！".format(casename))
    except:
        print("测试用例【{}】就执行失败了！".format(casename))

