'''
a = [1,2,3,"哈哈"]
a = str(a)

print(type(a))


b = "2333"
c = int(b)
print(type(c))


a = "2333"

c = int(a) * 2
print(c)


v = "你好我是时长练习2年半的RAPER"
x = len(v)
print(x)


hlist = [1,2,3,4,55,"kjk"]
x = len(hlist)
print(x)



name = input("请输入你的名字：")
age = input("请输入你的年龄：")
aihao = input("请输入你的爱好：")

print("你好，{name11}！,我今年{age}岁，我的爱好是{aihao}。我今年{age}岁".format(name11=name,age=age,aihao=aihao))

'''

'''
输入一个数字，如果大于60就放到hlist数组中，如果小于等于60，就放到lowlist数组中。

hlist = []
lowlist = []
a = int(input("请输入数字："))
if a > 60:
    hlist.append(a)
else:
    lowlist.append(a)
print("大于60的数组：",hlist,"小于60的数组：",lowlist)
'''

hlist = [1,2,3,4,5,6]
highnum = []
lownum = []
for i in hlist:
    if i > 4:
        highnum.append(i)
    else:
        lownum.append(i)
print('大于4的数字有{}个，小于四数字有{}个'.format(len(highnum),len(lownum)))



for i in range(1,10):
    for j in range(1,i+1):
        print("{}X{}={}".format(i,j,i*j),end="  ")
    print("")

a = 0
while a < 10:
    print("哈哈哈",a)
    a = a + 1
    if a == 6:
        break


# for i in range(1,5):
#     print("-----------------")
for j in range(1,8):
    if j == 3:
        break
    print("正在循环",j)

'''
判断今天是今年的第几天，2019，8，28
'''
year = int(input("请输入年："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
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