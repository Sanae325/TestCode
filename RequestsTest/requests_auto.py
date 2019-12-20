'''
1、准备测试用例，测试用例放在excel中 testcases文件夹下的接口测试用例模板.xlsx
2、读取excel，获取所有的测试用例 utils文件夹下的excel_tools.py
3、使用自动化代码去执行这些测试用例
'''
import requests
from utils.excel_tools import read_excel
from utils.dbtools import qurey

testcases = read_excel("testcases/接口测试用例模板.xlsx" , "Sheet1")
for testcase in testcases:
    # 构造请求
    # 这些值都是从我们自己定义的excel中读取额的
    url = testcase[1] # 接口的地址 
    case_name = testcase[3] # 测试用例的名字
    method = testcase[5] # 请求的方法
    request_headers = testcase[6] # 请求头
    playload = eval(testcase[7]) # 请求的参数
    http_response_code = int(testcase[8]) # http响应状态码预期结果
    interface_status_code = int(testcase[9]) # 接口的code预期结果
    request_sql = testcase[10] # excel中的sql语句
    try:
        res = requests.request(method , url = url , json = playload)
        # 断言http响应状态
        assert int(res.status_code) == http_response_code
        # 断言接口的响应值
        assert int(res.json().get("code")) == interface_status_code 
        # 去数据库中判断是否存在这个账号和密码
        outcome = qurey(request_sql)
        if int(res.json().get("code")) == 200:
            assert len(outcome) != 0
            print("测试用例【{}】执行通过!".format(case_name))
        else:
            assert len(outcome) == 0
            print("测试用例【{}】执行通过!".format(case_name))
    except:
        print("测试用例【{}】执行失败!".format(case_name))
