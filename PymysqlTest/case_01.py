import pymysql    
dbinfo = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"123456",
    "db":"test"
}
#db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="test")     #连接数据库
def qurey(sql):
    '''
    这个方法是查询数据库用的
    '''
    db = pymysql.connect(**dbinfo)    #连接数据库
    cursor = db.cursor()    #获取游标
    #sql = input("请输入sql语句：")
    try:
        cursor.execute(sql)     #执行sql语句
        res = cursor.fetchall()     #获取所有的返回值
        db.close()      #关闭数据库连接
        return res
    except:
        return None
# res = qurey("select * from t_student;")
# relist = []
# for i in res:
#     relist.append(i[2])
# print(relist)

def commit(sql):
    '''
    这个方法是修改数据库用的，新增、修改、删除
    '''
    db = pymysql.connect(**dbinfo)    #连接数据库
    cursor = db.cursor()    #获取游标
    try:
        cursor.execute(sql)     #执行sql语句
        db.commit()     #应用
        db.close()      #关闭数据库连接
        return True
    except:
        return False
sql = "insert into t_class (id,classname,teacher) values (5,'面试班','希希')"
# commit(sql)
# sql = "select * from t_class;"
res = commit(sql)
print(res)




