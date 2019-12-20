# (.*?) ：万能符
# \d ：去匹配数字
# \D ：非数字
# \s ：空格
# \S ：非空格
# \w ：字符 a-z A-Z 0-9·
# \W ：所有的特殊字符 空格 ，！ ￥

# import re
# a = "张小智张大智张德智"
# b = re.match("张(.*?)智", a).group()
# print(b)
# c = re.search("张(.*?)智", a).group()
# print(c)
# d = re.findall("张(.*?)智", a)
# print(d)

# def match():
#     '''
#         match：只能够匹配开头
#     '''
#     a = "啊老铁我太难了"
#     b = re.match("啊", a).group()
#     print(b)

# if __name__ == "__main__":
#     match()

# 输出字符串中重复的值，若没有，则输出空列表
# a = "1234453aba"
# # a = "123456"
# b = []
# c= []
# c.extend(a)    
# for i in a:         
#     c.remove(i)     
#     for k in c:
#         if i == k:
#             b.append(i)
# print(b)

a = "1234453aba"
# a = "123456"
b = []
c = []
for i in a:
    b.append(i)
    if b.count(i) > 1:
        c.append(i)
print(c)