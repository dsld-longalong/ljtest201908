# 用python来描述一个人
# ******************* 基础内容

class Human():
    """
        定义一个人这样的类
    """
    # 属性 = 类的成员变量
    age = 18
    sex = "男"
    height = "180"
    weight = "49"

    # 方法 = 成员方法
    def eat(self): 
        print(self.age)
        self.run()
        print("人能吃饭")   

    def run(self):
        print("人能跑路")

    def talk(self, msg, sound):
        """
            成员方的传参
        """
        print("这个人{}说了一句：{}".format(sound, msg))

# 实例化对象：去使用类
p = Human()
print(p.age)
p.eat()
p.talk("老铁，我太难了！", "大声的")