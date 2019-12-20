# def f(x):
#     return x * x
# L = []
# for n in range(10):
#     L.append(f(n))
# print(L)


# map()函数接收两个参数，一个是函数，一个是对象
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
