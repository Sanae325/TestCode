'''以60为分界线，拆分为两个数组'''
zlist = [78,76,56,99,100,76,64,45,67,87,75,56,90,90,87,65]
lowlist = []
highlist = []
for i in zlist:
    if i < 60:
        lowlist.append(i)
    else:
        highlist.append(i)
print(lowlist)
print(highlist)
'''以60为分界线，拆分为两个数组'''        
zlist = [11,76,56,99,100,76,64,45,67,87,75,56,90,90,87,20]
highlist = zlist
lowlist = []
for i in highlist:
    if i < 60:
        j = zlist.index(i)
        num = highlist.pop(j)
        lowlist.append(num)
print(lowlist)
print(highlist)



