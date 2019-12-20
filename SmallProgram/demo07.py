# 输入 八进制 值
x = str(input("请输入需要转换的数据："))
# 八进制 与 二进制 转换关系
dict1 = {"0":"000",
        "1":"001",
        "2":"010",
        "3":"011",
        "4":"100",
        "5":"101",
        "6":"110",
        "7":"111",
}
list1 = []
list2 = []
# 将 x 值拆分并传入 数组list1 中
list1.extend(x)
# 循环遍历
for i in list1:
    # 将 字典dict1 中对应值传入 数组list2 中
    list2.append(dict1.get(i))
# 数组 转换成 字符串
str1 = ''.join(list2)
# 打印 二进制 输出值
print(int(str1))

