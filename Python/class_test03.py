# 类的初始化 > 构造方法

class Human():
    age = None
    sex = None
    height = None
    weight = None

    def __init__(self, nl, xb, sg, tz):
        """
            初始化成员变量:构造方法，定义了类就有这个方法
        """
        self.age = nl
        self.sex = xb
        self.height = sg
        self.weight = tz


# 类的初始化传参
p = Human(nl=18, xb="女", sg=180, tz=49)
print(p.age)
print(p.sex)
print(p.height)
print(p.weight)