# # 计算阶乘n! = 1 x 2 x 3 x ... x n
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# k = fact(5)
# print(k)
'''
# 匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
'''
f = lambda x: x * x
print(f(5))