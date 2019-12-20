import pymysql
dbinfo = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"123456",
    "db":"test"
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
        print("sql语句输入错误，请重新输入！")
        exit()
def commit(sqll):
    '''
    这个方法是修改数据库用的，新增、修改、删除
    '''
    db = pymysql.connect(**dbinfo)    #连接数据库
    cursor = db.cursor()    #获取游标
    try:
        cursor.execute(sqll)     #执行sql语句
        db.commit()     #应用
        db.close()      #关闭数据库连接
        return True
    except:
        return False
sqll = "insert into t_class (id,classname,teacher) values (3,'面试班','希希')"
rescommit = commit(sqll)
sql = "select * from t_class;"
res = qurey(sql)
print(rescommit)
print(res)

