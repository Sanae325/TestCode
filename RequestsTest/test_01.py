import pymysql
dbinfo = {
    "host":"118.24.29.59",
    "user":"vn",
    "password":"1qaz!QAZ123",
    "db":"lux"
}
def qurey(sql):
    '''
    这个方法是查询数据库用的
    '''
    db = pymysql.connect(**dbinfo)    #连接数据库
    cursor = db.cursor()    #获取游标
    try:
        cursor.execute(sql)     #执行sql语句
        res = cursor.fetchall()     #获取所有的返回值
        db.close()      #关闭数据库连接
        return res
    except:
        return None

# sql = input("请输入sql语句：")
# res = qurey(sql)
# # # for i in res:
# # #     print(i)


    

# sql = input("请输入sql语句：")
# res = qurey(sql)
# resdict = {}
# for i in res:
#     resdict[i[2]] = i[6]
# print(resdict)

# sql = input("请输入sql语句：")
# res = qurey(sql)
# reslist = []
# for i in res:
#     reslist.append(i[2])
# print(reslist)