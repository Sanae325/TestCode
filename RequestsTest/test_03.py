
import requests
import pymysql

def qurey(sql,**dbinfo):
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
        res = cursor.fetchall()     #获取所有的返回值
        db.close()      #关闭数据库连接
        return res
    except:
        print("sql语句输入错误，请重新输入！")
        exit()
def test_post_json():
    # 接口地址
    url = "http://118.24.29.59:5000/userLogin/"
    # 请求的参数
    payload = {"username":"test", "password":"123456", "captcha":"123456"}
    # 使用post方法去请求这个接口
    response = requests.post(url = url,json = payload)
    
    # 判断http响应状态码
    # python自带的断言，assert
    # 如果http响应状态码等于200，那么断言成功
    # 如果断言失败，assert就会抛出一个断言失败的异常，代码就终止
    assert response.status_code == 200


    # 判断接口返回的code值
    # response.json()把接口的响应值转换成字典，响应值必须是json格式的，如果不是字典形式就会报错
    assert response.json().get("code") == 200

    sql = "select * from tbl_user where username = 'test' and password = '123456'"
    res = qurey(sql)
    # res长度不为0 = 从数据库中查到了这条数据
    assert len(res) != 0
    print("测试通过！")
    

if __name__ == "__main__":
    test_post_json()