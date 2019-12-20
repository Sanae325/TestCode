'''
1、生成报告文件pytest xxx.py --alluredir report 或者pytest --alluredir report
2、测试结果转换成网页allure generate ./report -o ./report_html --clean
3、打开网页的测试报告allure open -h 127.0.0.1 -p 9999 ./report_html
'''
# 导入pytest
import pytest

# 使用方法来管理测试用例
# 方法必须是 test_ 开头
# 第一个方法就称为一个测试用例
# 运行命令： pytest xxx.py   或者  pytest -q xxx.py
# 运行文件夹： pytest xxx  或者  pytest -q xxx  或者在文件夹下pytest（pytest -q）
def test_add():
    assert 1+1 == 2

