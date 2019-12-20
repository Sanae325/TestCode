import threading
import time


def test1(temp):
    temp.append(33)
    print(temp)


def test2(temp):
    print(temp)

num = [11,22]


def main():
    # target 指定将来这个线程去哪个函数执行代码
    # args 指定将来调用函数的时候，传递什么数据过去
    t1 = threading.Thread(target=test1, args=(num,))
    t2 = threading.Thread(target=test2, args=(num,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print(num)

    
if __name__ == "__main__":
    main()