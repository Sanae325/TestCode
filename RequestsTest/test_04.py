'''
接口地址：http://118.24.29.59:5000/userLogin/
接口类型：POST
headers：Content-Type:application/json
请求参数：{"username":"test", "password":"test", "captcha":"123456"}
'''
# import requests
# url = "http://118.24.29.59:5000/userLogin/"     #接口地址
# headers = {"Content-Type":"application/json"}   #请求头
# data = {"username":"test", "password":"123456", "captcha":"123456"}   #请求参数
# res = requests.post(url,headers = headers,json = data)  #获取接口的返回值
# hdict = res.json()  #把返回值转换为可以操作的字典格式
# # print(hdict)     #打印返回数据
# if hdict["msg"] == "登录成功!":
#     print("登录接口测试通过！")
# else:
#     print("测试失败！")

'''
http://118.24.29.59:5000/userRegist/
{"username":"user3322", "password":"123", "nickname":"user33"}
'''
import requests
from test_01 import qurey

url = "http://118.24.29.59:5000/userRegist/"     #接口地址
headers = {"Content-Type":"application/json"}   #请求头
data = {"username":"jiuge2", "password":"1234", "nickname":"九歌"}   #请求参数
res = requests.post(url,headers = headers,json = data)  #获取接口的返回值
hdict = res.json()  #把返回值转换为可以操作的字典格式
sql = "select * from tbl_user where username = 'jiuge2';"
res = qurey(sql)
if hdict["msg"] == "注册成功!":
    if res[0][1] == "jiuge2":
        print("注册接口测试通过！")
    else:
        print("数据写入数据库失败!")
else:
    print("测试失败！")
