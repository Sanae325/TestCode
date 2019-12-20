"""
    unittest入门demo
"""

# 导入unittest包
import unittest
class TestCaseDemo1(unittest.TestCase):

    # 成员方法（测试用例）必须以test_开头
    def test_01_add(self):
        assert 1+1 ==2
        print("add方法执行通过了")   

