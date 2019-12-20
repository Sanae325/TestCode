import threading
import time


num = 100 # 定义一个全局变量


def test1():
    global num
    num += 100
    print(num)


def test2():
    print(num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print(num)


if __name__ == "__main__":
    main()