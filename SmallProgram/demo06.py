'''
用filter求素数(100以内的素数)
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10 ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 5, 7, 9, 11, 13, 15, 17, 19 ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 7, 11, 13, 17, 19, ...
不断筛下去，就可以得到所有的素数。
'''
# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
# (注意这是一个生成器，并且是一个无限序列)
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0
# 最后，定义一个生成器，不断返回下一个素数：
# (这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列)
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# 打印100以内的素数:
list = []
for n in primes():
    if n < 100:
        list.append(n)
    else:
        break
print(list)