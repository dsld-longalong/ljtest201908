"""
    xlrd读取excel
"""
import xlrd

def read_excel(excel_path, sheet_name):
    """
        读取excel方法
        参数：
            excel_path: excel的路径
            sheet_name：这个表格的哪个页面
    """
    results = []
    datas = xlrd.open_workbook(excel_path) # 打开excel，并返回excel的操作对象
    table = datas.sheet_by_name(sheet_name) # 打开名字为sheet_name参数的页面

    # 循环添加每一行的信息
    for row in range(1, table.nrows):
        d = table.row_values(row)   # 每一行的值
        results.append(d)

    return results


if __name__ == "__main__":
    for d in read_excel("testcase/接口测试用例模板.xlsx", "Sheet1"):
        print(d)