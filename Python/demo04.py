'''
# from demo03 import jsjtsjnddjt,jiafa
import demo03
xx = demo03.jiafa(1,3,4,5)
print(xx)
import time
# time.sleep(10)
xxx = time.strftime("%y-%m-%d %H:%M:%S")
print(xxx)
print("刚刚暂定了十秒钟！")
'''

'''
实现一个红绿灯的功能，每隔一秒，打印一次现在的灯的颜色。
'''
import time
light = {
    "红灯":30,
    "绿灯":30,
    "黄灯":3
}
while True:
    for i in light:
        for j in range(light[i]):
            print("【{}】距离结束倒计时【{}】秒".format(i,light[i]-j))
            time.sleep(1)

