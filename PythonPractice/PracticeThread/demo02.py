import threading
import time


class MyThread(threading.Thread):
    def run(self): # 必须定义run函数
        for i in range(3):
            time.sleep(1)
            msg = "I'am"+self.name+"@"+str(i) # name属性中保存的是当前线程的名字
            print(msg)
            
        self.register()
        self.login()

    def register(self):
        print("---注册---")


    def login(self):
        print("---登录---")

    
if __name__ == "__main__":
    t = MyThread()
    t.start()   