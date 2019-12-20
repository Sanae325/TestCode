'''
unittest的生命周期
'''
import unittest

class TestCaseLifeCycle(unittest.TestCase):

    # 类方式和结束的方法称为：类方法
    # 只执行一次
    # cls等同于self
    @classmethod
    def setUpClass(cls):
        print("setUpClassset")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")



    # 成员方法开始和结束的方法
    # 每一个test_开始的方法在运行前都会去执行setUp
    # 每一个test_开始的方法在结束后都会区执行tearDown
    def setUp(self):
        print("setUp")
    
    def tearDown(self):
        print("tearDown")

    def test_01_a(self):
        print("01")
    
    def test_02_b(self):
        print("02")



if __name__ == "__main__":
    unittest.main()