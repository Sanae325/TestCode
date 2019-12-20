'''
斐波拉契数列，生成器
'''
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a+b
        current_num += 1


# obj = create_num(10) # 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
# obj2 = create_num(20)

# for num in obj:
#     print(num, "", end="")
# print()
# for num in obj2:
#     print(num, "", end="")


obj3 = create_num(5)

while True:
    try:
        ret = next(obj3)
        print(ret, "", end="")
    except Exception as ret:
        break