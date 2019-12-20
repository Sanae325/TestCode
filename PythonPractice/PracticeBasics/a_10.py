# def int2(x, base=2):
#     return int(x, base)  #传入base参数，就可以做N进制的转换

import functools
int2 = functools.partial(int, base=2)   #功能等于def int2()，创建偏函数
print(int2('1111'))