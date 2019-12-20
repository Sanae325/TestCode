# 1. 类里面的成员方法是怎么传参的呢
# 2. self这个关键字的含义 self就是这个类的实例化对象本身，实例化对象p是在用类外面的，self是用在类里面的

class Phone():
    band = "华为"
    color = "幻夜星河"
    price = 3200

    # 成员方法去引用成员变量
    def describe1(self):
        print("这是一台价值{}的{}{}手机".format(self.price, self.color, self.band))
    
    # 成员方法调成员方法
    def describe2(self):
        self.describe1()

p = Phone()
p.describe1()
p.describe2()