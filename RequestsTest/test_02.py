import requests
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

    # 可选的，根据实际情况来考虑是不是需要去数据库查询
    sql = "select * from tbl_user where username = 'test' and password = '123456'"
    res = qurey(sql)
    # res长度不为0 = 从数据库中查到了这条数据
    assert len(res) != 0
    print("测试通过！")

if __name__ == "__main__":
    test_post_json()




# # http的get方法
# import requests
# def test_get():
#     res = requests.get("https://www.baidu.com")
#     print(res.text) # 响应body
#     print(res.status_code) # http响应状态码
# if __name__ == "__main__":
#     test_get()




# # http的post之form-data方法
# import requests
# def test_post_formdata():
#     url = "http://132.232.44.158:7777/login"

#     payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n张德智\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
#     headers = {
#         'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#         'cache-control': "no-cache",
#         'Postman-Token': "8178be46-c672-49d2-a61c-80f0e2900918"
#         }

#     response = requests.request("POST", url, data=payload, headers=headers)

#     print(response.text)
# if __name__ == "__main__":
#     test_post_formdata()
