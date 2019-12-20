'''
    py文件的作用：整个自动化测试项目框架的入口
    1. cases：用来放测试用例
    2. drivers：用来放selenium驱动
    3. report：用来放测试报告
    4. utils：用来放工具代码（pymysql、htmltestrunner）
    5. run.py : 运行入口
'''
'''
scmcc_web:
    |---- config层                   配置层，放项目配置文件
    |---- data层                     数据层，放数据文件，把testcase参数化的文件放到这里，一般用xml、excel，好处是把数据与代码隔离开，数据驱动测试原则）
    |---- drivers层                  驱动层，放selenium2所需驱动，如ChromeDriver、FirefoxDrider等
    |---- log层                      日志层，放执行日志文件，如xxx.log等（暂未启用）
    |---- report层                   报告层，放测试执行报告，后期自动发送Email功能所需文件的目录
    |---- scr层                      代码层，各种执行代码
    |       |---- test                      测试代码层
    |       |       |---- case              测试用例
    |       |       |---- common            测试共用方法
    |       |       |---- page              po层，放页面对象，便于维护页面元素
    |       |       |---- suite             测试集合，用于组织测试用例
    |       |---- utils                     工具层，存放各种工具代码
    |---- venv层                     环境层，放windows环境下的虚拟环境
    |---- ReadMe.md                  项目介绍文件，可以用于项目介绍和后期项目功能备注
    |---- requirements.txt           项目依赖文件，使用pip3 install -r requirements.txt
    |---- run.py                     项目执行入口
'''

# 1. 导入所需的包
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 2. 让unittest自动去查找cases下面所有测试用例
testcases = unittest.defaultTestLoader.discover("cases", "test_*.py")

# 3. 把所有测试用例加载到测试集里面
testsuits = unittest.TestSuite()
testsuits.addTests(testcases)

# 4. 运行测试集并且生成测试报告
title = "测试报告"
descr = "猫宁生鲜的测试报告"
file_path = "./report/morning_reports.html"

with open(file_path, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testsuits)

    