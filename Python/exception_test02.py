a = [1,2,3]
i = 0
while i < 5:
    try:
        b = a[i]
    except Exception as cvccc:
        print(cvccc)
        print("第{}次出错了".format(i+1))
    else:
        print("第{}次没有出错".format(i+1))
    finally:
        print("我全都要！")
        print("****************")

    i = i + 1

print("代码执行到这儿了")