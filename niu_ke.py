# str1 = str(input())

# for i in str1:
#     if i in "0123456789":
#         str1.replace(i)
# print(str1)

# import random
# arr = []
# i = 0
# while i<10:
#     arr.append(random.randint(1,10))
#     i = i+1
# for i in range(1, len(arr)):
#         for j in range(0, len(arr)-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print(arr)

# str1 = input()
# list1 = []
# list2 = []
# list3 = []
# for i in str1:
#     if i !=" ":
#         if int(i) % 2 == 0:
#             list1.append(i)
#         else:
#             list2.append(i)
# list1.sort()
# list2.sort()
# list2.reverse()
# list3 = list1 +list2
# str2 = " ".join(list3)
# print(str2)


# num = input().split()
# list1 = []
# list2 = []
# for i in num:
#     if int(i) % 2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# list1 = list1 +list2
# for i in list1:
#     print(i)


# n = map(int,input().split())
 
# a, b = [], []
 
# for i in n :
#     if i % 2 == 0 :
#         a.append(i)
#     else : b.append(i)
#     pass
 
# a += b
 
# for i in a :
#     print(i, )


# import sys
# try: 
#     while True:
#         str1 = sys.stdin.readline().strip()
#         if str1 == '':
#             break 
#         print(str1)
# except: 
#     pass


# import sys
# str1 = sys.stdin.readline().strip().split()
# print(str1)





'''
计算字符串最后一个单词的长度，单词以空格隔开。 
一行字符串，非空，长度小于5000。
hello world
整数N，最后一个单词的长度。
5
'''
# list1 = list(input())
# list1.reverse()
# for i in range(len(list1)):
#     if list1.count(" ") == 0:
#         print(len(list1))
#         break
#     if list1[i] ==" ":
#         print(i)
#         break

'''
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。
ABCDEF
A
输出输入字符串中含有该字符的个数。
1
'''
# str1 = input()
# str2 = input()
# print(str1.lower().count(str2.lower()))






# import sys

# while True:
#     list1 = []
#     str1 = sys.stdin.readline().strip()
#     if str1 == '':
#         break 
#     list1.append(str1)
# list1=[int(i) for i in list1]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# list2.sort()
# for i in list2:
#     print(i)


'''
题目描述：
小美和小团在玩一个游戏，小美任意给出一个大字符串str1以及一个独立的小字符串str2，小团需要从这个大字符串str1里找到包含独立小字符串str2中所有字符的最小子字符串str3；

 * 例如，小美给出一个大字符串"meituan2019"和一个子字符串"i2t"，那么小团给出的答案就应该是"ituan2"；

需要注意：

1、str1中有可能没有完整包含str2所有字符的情况，此时返回""；

2、str1不会为空，但str2有可能为空，此时返回整个str1；

3、str2可能存在重复的字符，此时str3需要包含相等数量该字符；



输入
第一行，一个大字符串

第二次，一个子字符串

字符串长度不超过106

输出
输出结果


样例输入
meituan2019
i2t
样例输出
​ituan2
'''


# list_max = list(input())
# list_min = list(input())
# if list_min != []:
#     list_num = []
#     list_out = []
#     for i in list_min:
#         if i in list_max:
#             list_num.append(list_max.index(i))
#     list_num.sort()
#     list_out = list_max[list_num[0]:list_num[len(list_num)-1]+1]
#     print("".join(list_out))
# else:
#     print("".join(list_max))

'''
将给定的字符串，按照规则删除字符，输出删除后的字符串。删除规则为：相同字符连续，则删除，如”aaaab”删除后的字符串为”b” 。注：仅是单个字符连续才删除，如babababa则不能删除；

输入
输入数据有多组，每组一行，仅包含数字和英文字母，不包含转义等其他特殊字符，输入数据最大长度为10；

输出
对于每个测试实例，要求输出按规则删除后的数据，每个测试实例的输出占一行。如果删除后有字符，直接输出删除后的字符；如果删除后为空，则输出”no”


样例输入
aaaaabbbb
样例输出
no

提示
输入样例2
a

输出样例2
a
'''
# str1 = input()
# list1 = []
# list2 = []
# for i in str1:
#     list1.append(i)
# for i in range(len(list1)-1):
#     if list1[i] == list1[i+1]:
#         list1[i] = ""
#         list1[i+1] =""
# for i in list1:
#     if i != "":
#         list2.append(i)
# print("".join(list2))
        


'''
输入：A={1,3,5},B={2,4,6},R=1
输出：(1,2)(3,4)(5,6)
'''
# import re
# str_input = input()
# a = re.findall("A={(.*?)}",str_input)
# b = re.findall("B={(.*?)}",str_input)
# for i in range(len(str_input)):
#     if str_input[i] == "R":
#         R = int(str_input[i+2:len(str_input)])
# A = a[0].split(",")
# B = b[0].split(",")
# b = 0
# for a in range(len(A)):
#     if int(A[a]) > int(B[b]):
#         b = b + 1
#         if b-a > R:
#             break
#     print("("+A[a]+","+B[b]+")",end="")



'''
输入字符串，里面包含子串;子串用,隔开；子串内容可能是纯数字串，纯英文单词，或者字母数字符号混合
统计子串中首位和末位数字之和大于8的纯数字串的个数（只有一位纯数字串不做统计）
时间复杂度小于等于O(n)
输入：hello,79,1.9,are,09,there
输出：2
'''
# list1 = input().split(",")
# n = 0
# for i in list1:
#     try:
#         if int(i[0]) + int(i[len(i)-1]) > 8:
#             n = n + 1
#         if i in ["1","2","3","4","5","6","7","8","9",] or "." in i:
#             n = n - 1
#     except:
#         pass
# print(n)


# M = int(input())
# q = int(input())
# def num():
#     if M = 1:
#         return 1
#     return     


'''
对于一个字符串，请设计一个算法，只在字符串的单词间做逆序调整，也就是说，字符串由一些由空格分隔的部分组成，你需要将这些部分逆序。
给定一个原字符串A，请返回逆序后的字符串。例，输入"I am a boy!", 输出"boy! a am I"

'''

# list1  = input().split(" ")
# list1.reverse()
# for i in list1:
#     print(i+" ",end="")


'''
输入多组坐标，输入格式为:x1 y1,x2 y2,········如：1 2,2 3,4 5
坐标值为二维空间里x,y坐标系的点，求包含这些点的最小长方形（长方形的边平行于坐标轴，点在边上也属于包含）
输出长方形坐标值，先输出最小的坐标，然后顺时针输出其他坐标
输入如：1 2,2 3,4 5
输出如：1 2,1 5,4 5,4 2

输入如：-1 1,2 0
输出如：-1,-2,1 2,1 1        
我输出的是这种格式的：- 1,- 2,1 2,1 1，负号会产生空格
（和那天的那个元组的输出类似，这次是有8个值，不知道哪些是负号，怎么去除输出负数时产生的空格）
'''
# list1 = list(input())
# x_list = []
# y_list = []
# for i in list1:
#     if i == " " or i == ",":
#         list1.remove(i)
# for i in range(len(list1)):
#     if i % 2 == 0:
#         x_list.append(list1[i])
#     else:
#         y_list.append(list1[i])
# x_min = min(x_list)
# x_max = max(x_list)
# y_min = min(y_list)
# y_max = max(y_list)
# print(x_min+" "+y_min+","+x_min+" "+y_max+","+x_max+" "+y_max+","+x_max+" "+y_min)

'''
快手
'''

# list1 = list(input())
# x_list = []
# y_list = []
# for i in list1:
#     if i == " " or i == ",":
#         list1.remove(i)
# for i in range(len(list1)):
#     if i % 2 == 0:
#         x_list.append(list1[i])
#     else:
#         y_list.append(list1[i])
# x_min = min(x_list)
# x_max = max(x_list)
# y_min = min(y_list)
# y_max = max(y_list)
# print(x_min+" "+y_min+","+x_min+" "+y_max+","+x_max+" "+y_max+","+x_max+" "+y_min)


# list1 = input().split(",")
# k = 0
# for i in range(len(list1)-1):
#     if list1[i] > list1[i+1]:
#         k = k + 1
# if k == 1:
#     print(1)
# else:
#     print(0)


# str1 = input()
# for i in range(len(str1)):
#     for k in range(i+1,len(str1)):
#         if str1[i] == str1[k]:
#             str2 = str1[i:k+1]
#             if str2 in str1:
#                 print(str2)
#             exit()








# list1 = input().split(" ")
# n = 0
# for i in range(len(list1)-1):
#     if list1[i] > list1[i+1]:
#         n = n + 1
# print(n+1)



# x = int(input())
# if x <= 5:
#     h = 4*x
# elif x <= 15:
#     h = (x-5)*2 + 20
# elif x <= 25:
#     h = (x-15)*1 + 40
# else:
#     h = 50
# print(h)


# import sys
# try: 
#     while True:
#         str1 = sys.stdin.readline().strip()
#         list1 = []
#         if str1 == '':
#             break 
#         for i in str1:
#             if i in "sangfor":
#                 list1.append(i)
#         str2 = "".join(list1)
#         print(str2)
#         n = str2.count("sangfor")
#         print(n)
# except: 
#     pass





# n_m = input().split(" ")
# x_i = input().split(" ")
# n = 0
# while n < int(n_m[1]):
#     m = input()
#     num = x_i.count(m)
#     print(num)
#     n = n + 1



# T = input()
# n = input()
# k = 0
# while k < int(T):
#     num_list_input = input().split(" ")
#     num_list = []
#     for i in num_list_input:
#         num_list.append(int(i))
#     for i in range(len(num_list)-1):
#         if sum(num_list[0:i]) == sum(num_list[i:len(num_list)]):
#             print("YES")
#         elif i == len(num_list)-2:
#             print("NO")
#     k = k + 1


# str1 = input()
# list1 = []
# for i in str1:
#     try:
#         if 0<=int(i)<=24:
#             list1.append(i)
#     except:
#         pass
# str2 = "".join(list1)
# list1.sort()
# str3 = "".join(list1)


'''
假设一个有效的四位版本号是由四个正整数组成，且以小数点分割，不包含空格和其他字符。
请写一个函数，判断某个字符串是否是一个有效的版本号
输入：1.1.1.1
输出：ture

输入：1.a.a.1
输出：false
'''
# str1 = input()
# if str1.count(".") == 3:
#     list1 = str1.split(".")
#     list2 = []
#     try:
#         for i in list1:
#             if int(i)>0:
#                 list2.append(i)
#     except:
#         pass
#     if len(list1) == len(list2):
#         print("ture")
#     else:
#         print("false")
# else:
#     print("false")
# 通过了81.25%的测试用例

# str1 = input()
# if str1.count(".") == 3:
#     list1 = str1.split(".")
#     list2 = []
#     try:
#         for i in list1:
#             if int(i)>0:
#                 list2.append(i)
#     except:
#         pass
#     if len(list1) == len(list2):
#         print("ture")
#     else:
#         print("false")
# else:
#     print("false")



# # 19
# num = input()
# print(len(num))
# num_list = list(num)
# num_list.reverse()
# num_reverse = "".join(num_list)
# print(num_reverse)

# # 20
# n = 0
# list1 = []
# while n < 5:
#     x = input()
#     list1.append(int(x))
#     n = n + 1
# print("最大值：",max(list1))
# print("最小值：",min(list1))

# # 22
# num = input()
# num_list = list(num)
# num_list.reverse()
# num_reverse = "".join(num_list)
# if num == num_reverse:
#     print(num,"是回文数")
# else:
#     print(num,"不是回文数")


# # 18
# num = list(input())
# num.sort()
# sum = 0
# for i in num:
#     print(i)
#     sum = sum + int(i)
# print("总和：",sum)

# # 23
# num = input().split(",")
# sum = 0
# n = 0
# while n < 20:
#     for i in num:
#         list1 = i.split("/")
#         print(list1)
#         sum = sum + (int(list1[0]) / int(list1[1]))
#         n = n + 1
# print(sum)

'''
计算 aaa...aaa(n个a)*b=?
请你输出该式的计算结果的各位数字之和是多少。
3 4 3
9
'''
# list1 = input().split(" ")
# num = str(int(list1[0]) ** int(list1[2]) * int(list1[1]))
# h = 0
# for i in num:
#     h = h + int(i)
# print(h)



'''
输入三个坐标，判断是否为三角形，不是输出“Impossible”，是三角形输出周长和面积，保留两位小数
4 5 6 9 7 8
10.13
3.00

4 6 8 12 12 18
Impossible
'''
# import math
# list1 = input().split(" ")
# list_x = []
# list_y = []
# for i in range(6):
#     if i % 2 == 0:
#         list_x.append(int(list1[i]))
#     else:
#         list_y.append(int(list1[i]))
# if (list_x[0] - list_x[1]) / (list_x[1] - list_x[2]) == (list_y[0] - list_y[1]) / (list_y[1] - list_y[2]):
#     print("Impossible")
# else:
#     a = math.sqrt((list_x[0]-list_x[1]) ** 2 + (list_y[0]-list_y[1]) ** 2)
#     b = math.sqrt((list_x[0]-list_x[2]) ** 2 + (list_y[0]-list_y[2]) ** 2)
#     c = math.sqrt((list_x[1]-list_x[2]) ** 2 + (list_y[1]-list_y[2]) ** 2)
#     L = a + b + c
#     p = L / 2
#     S = math.sqrt(p * (p - a) * (p - b) * (p -c))
#     print(round(L,2))
#     print(round(S,2))




# import random
# import time

# shengming = 60
# while True:
#     print("------死亡游戏------")
#     xxx = time.strftime("%y-%m-%d %H:%M:%S")
#     print("当前的时间 ",xxx)
#     if shengming > 8:
#         x = input("买大还是买小? ")
#         if x == "大" or x == "小":
#             y = random.randint(1,6)
#             if y>=4:
#                 z = "大"
#             else:
#                 z = "小"
#             if x==z:
#                 print("买对了！！！")
#                 print("生命+5")
#                 shengming +=5
#             else:
#                 print("错了!")
#                 print("生命-20")
#                 shengming -=21
#             print("你的生命距离结束还有: ",shengming)
#         else:
#             print("输入错误，请重新开始游戏！")
#             break
#     else:
#         print("你已经死了!")
#         break



# print("\n".join([''.join([('ILoveYou'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))



# def compare_max(a,b):
#     if a <= b:
#         return b
#     else:
#         return a


# list1 = ["QA1222","QA12ds","QA12sd2","sdsdds","sdsdss","QQA1222"]
# list2 = []

# for i in list1:
#     if "QA1" == i[0:3]:
#         list2.append(i)

# print(list2)



# pay = int(input("请输入pay值："))
# if pay <= 5000:
#     Z = 0
# elif pay <= 8000:
#     Z = (pay - 5000) * 0.03
# elif pay <= 17000:
#     Z = (pay - 8000) * 0.1
# elif pay <= 30000:
#     Z = (pay - 17000) * 0.2
# elif pay <= 40000:
#     Z = (pay - 30000) * 0.25
# elif pay <= 60000:
#     Z = (pay - 40000) * 0.3
# elif pay <= 85000:
#     Z = (pay - 60000) * 0.35
# else:
#     Z = (pay - 85000) * 0.45
# print(Z)