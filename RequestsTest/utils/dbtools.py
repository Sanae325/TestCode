import pymysql

def qurey(sql):
    '''
    这个方法是查询数据库用的
    '''
    dbinfo = {
    "host":"118.24.29.59",
    "user":"vn",
    "password":"1qaz!QAZ123",
    "db":"lux"
    }
    db = pymysql.connect(**dbinfo)    #连接数据库
    cursor = db.cursor()    #获取游标
    try:
        cursor.execute(sql)     #执行sql语句
        outcome = cursor.fetchall()     #获取所有的返回值
        db.close()      #关闭数据库连接
        return outcome
    except:
        return None