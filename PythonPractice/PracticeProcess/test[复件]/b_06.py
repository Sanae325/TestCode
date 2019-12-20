# 类的构造方法：在实例化这个类的时候，我们可以通过构造方法来初始化这个类的一些事情
class FanWan():
    banjing = "10cm"
    mingzi = "小白"
    yanse = "白色"

    # 构造方法，需要传递 半径、名字、颜色这个三个变量
    def __init__(self, bj, mz, ys):
        self.banjing = bj
        self.mingzi = mz
        self.yanse = ys
        
wan = FanWan("20cm", "小黑", "黑色")
print(wan.banjing)
print(wan.mingzi)
print(wan.yanse)

# # 类的继承：继承最大的好处是子类获得了父类的全部功能，包括变量和方法
# # QingHuaCi是Wan的子类
# # Wan是QingHuaCi的父类
# class Wan():
#     name = "金箔"
#     def huayuan(self):
#         print("唐三藏的金箔可以化缘")

# class QingHuaCi(Wan):
#     # 重写父类的成员变量
#     name = "青花瓷器碗"

#     # 重写父类的方法
#     def huayuan(self):
#         print("我是青花瓷了，不需要化缘！")

# qhc = QingHuaCi()
# print(qhc.name)
# qhc.huayuan()