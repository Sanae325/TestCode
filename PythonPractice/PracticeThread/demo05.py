'''
使用互斥锁解决资源竞争问题
'''
import threading
import time


g_num = 0 # 定义一个全局变量


def test1(num):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时，上锁成功
    # 如果上锁之前，已经被上锁了，那么此时会堵塞在这里，直到这个锁被解开为之
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release() # 解锁
    print("---test1---",g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("---test2---",g_num)


mutex = threading.Lock() # 创建一个互斥锁，默认是没有上锁的


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(2) # 等待上面两个线程执行完毕
    print("---main---",g_num)


if __name__ == "__main__":
    main()