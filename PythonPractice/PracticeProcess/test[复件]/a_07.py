# list = [36, 5, -12, 9, -21]
# list1 = sorted(list)    #默认从小到大排序
# list2 = sorted(list,key = abs)  #按绝对值大小排序
# print(list)
# print(list1)
# print(list2)


list = ['bob', 'about', 'Zoo', 'Credit']
list1 = sorted(list)    #默认按照ASCII从小到大排序
list2 = sorted(list,key=str.lower)  #忽略大小写排序
list3 = sorted(list,key=str.lower, reverse=True)  #忽略大小写反向排序
print(list)
print(list1)
print(list2)
print(list3)
