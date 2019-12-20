class Wan():
    name = "金箔"

    # def set_name(self,name):
    #     self.__name = name

    def huayuan(self):
        print("唐三藏的金箔可以化缘")

class QingHuaCi(Wan):
    pass

qhc = QingHuaCi()
print(qhc.name)
qhc.huayuan()


# qhc = QingHuaCi()
# qhc.set_name = "青花瓷"
# print(qhc.set_name)

