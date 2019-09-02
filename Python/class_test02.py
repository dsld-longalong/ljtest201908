# 类的继承

class Fathor():
    """父类"""
    jiancha = 5000000
    
    def company(self):
        print("老爸有公司")

class Son(Fathor):
    """子类"""
    # pass    # 占位，语法上不报错，定义一个空类

    # 属性的重写
    jiancha = 0.5
    
    # 方法的重写
    def company(self):
        print("继承的公司倒闭了!")
    

# 定义个a变量来接受Son类的实例化对象
# 子类去引用父类的属性和方法
a = Son()
print(a.jiancha)
a.company()