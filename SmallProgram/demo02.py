
'''输出当前日期'''
# import time
# # time.sleep(5)
# sss = time.strftime("%Y-%m-%d %H:%M:%S")
# print(sss)
'''红绿灯倒计时'''
# import time
# while True:
#     for i in range(1,31):
#         print("红灯倒计时{}秒".format(31-i))
#         time.sleep(1)
#     for i in range(1,31):
#         print("绿灯倒计时{}秒".format(31-i))
#         time.sleep(1)
#     for i in range(1,4):
#         print("黄灯倒计时{}秒".format(4-i))
#         time.sleep(1)
'''红绿灯倒计时'''
# import time
# light = {
#     "红灯":30,
#     "绿灯":30,
#     "黄灯":3
# }
# while True:
#     for i in light:
#         t = light.get(i)
#         while t != 0:
#             print("{}倒计时{}秒".format(i,t))
#             time.sleep(1)
#             t = t - 1
'''
判断今天是今年的第几天
闰年直接理解为满足以下两个条件之一，即是闰年
1、年份能被4整除，且不能被100整除
2、年份能被400整除
'''
# zstr = input("请输入今天的日期，格式如2019-7-24：")
# xxx = zstr.split("-")
# newymd = []
# for i in xxx:
#     i = int(i)
#     newymd.append(i)
# year = newymd[0]
# month = newymd[1]
# day = newymd[2]
# zlist = [31,28,31,30,31,30,31,31,30,31,30,31]
# days = 0
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     zlist[1] = 29
#     for i in range(month-1):
#         days = days +zlist[i]
#     days = days +day
# else:
#     for i in range(month-1):
#         days = days +zlist[i]
#     days = days +day
# print("今天是{}年的第{}天".format(year,days))