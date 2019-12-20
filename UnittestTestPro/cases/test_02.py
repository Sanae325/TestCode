'''
unittest自带的断言，只有当用到unittest框架来组织测试用例的时候，才使用self.assertXXXX的来断言
除此之外，老老实实用python自带的assert断言
'''
import unittest

class TestCaseAssert(unittest.TestCase):

    def test_01_equal(self):
        # 判断相等
        a = 0
        b = 1
        self.assertEqual(a, b, "a和b不相等") # 第三个参数可传可不传，断言失败后，输出第三个参数msg 
        self.assertNotEqual(a, b)
  
    def test_02_zhenjia(self):
        # 判断真假
        self.assertTrue(True)   # True通过，False失败
        self.assertFalse(False) # False通过，True失败

    def test_03_is(self):
        # 判断是否为同一对象
        a = "小强强"
        b = "小坤坤"
        self.assertIsNot(a, b)  # a和b不是同一个对象，就通过；反之失败
        self.assertIs(a, b)     # a和b是同一个对象就通过；反之失败
    
    def test_04_isnone(self):
        # 判断是否为空
        a = None
        b = ""
        self.assertIsNone(a)    # 为None通过，反之失败
        self.assertIsNotNone(b) # 不为None通过，反之失败
        
    def test_04_in(self):
        """
            a = "中国香港"
            b = "中香"
            b in a
            False
        """
        # 判断是否包含
        a = "小坤坤"
        b = "坤坤"
        c = "小小坤"
        self.assertIn(b, a)    # b在a里面能找到，就通过；反之失败
        self.assertNotIn(c, a) # c不在a里面就通过；反之失败
        
        # 判断是否为实例
        # self.assertIsInstance()    # 是否为实例对象
        # self.assertIsNotInstance() # 是否为实例对象
        
