
def jsjtsjnddjt(year,month,day):
    '''
    判断今天是今年的第几天，2019，8，28
    '''
    # year = int(input("请输入年："))
    # month = int(input("请输入月份："))
    # day = int(input("请输入日期："))
    monthlist = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    if year%400==0 or (year%4==0 and year%100!=0):
        monthlist[1] = 29
        for i in range(month-1):
            days = days + monthlist[i]
        days = days + day
    else:
        for i in range(month-1):
            days = days + monthlist[i]
        days = days + day
    print("今天是今年的第{}天".format(days))





'''
任意输入多少个数字，算和
'''

def jiafa(*num):
    '''
    可以传入任意多个数字，计算和
    '''
    jieguo = 0
    for i in num:
        jieguo = jieguo + i
    return jieguo


# xx = jiafa(1,344,54,667,345,345)
# print(xx)




# hlist = [1,2,"哈哈","哈哈"]
# print(hlist.count("哈哈"))





