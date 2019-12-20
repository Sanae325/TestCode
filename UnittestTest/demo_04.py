'''
unittest实现猫宁生鲜加入购物车测试用例
要求：
    1、使用selenium，结合unittest
    2、断言用网页标题（用unittest自带的断言）
'''

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestCaseMorning(unittest.TestCase):

    def test_shopping(self):

        def find_element(driver,locator):

            element = WebDriverWait(driver,10).until(lambda s: s.find_element(*locator))
            return element

        driver = webdriver.Chrome(executable_path="D:/PythonPro/TestCode/SeleniumTest/drivers/chromedriver") 
        driver.maximize_window() 
        driver.get("http://118.24.29.59:8080") 

        crystal_iceberg = ("xpath", '//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
        add_shopping_bags = ("id", "J_mer_saleTag")
        shopping_bag = ("xpath", '//*[@id="J_header_cart"]/div[1]/a[1]')
        immediate_settlement = ("xpath", '//*[@id="J_cart_bar"]/div[1]/a')
        phone_number = ("id", "username")
        password = ("id", "password")
        login = ("id", "btnLogin")

        find_element(driver,crystal_iceberg).click()       # 点击“水晶冰菜”图片
        find_element(driver,add_shopping_bags).click()     # 点击“加入购物袋”
        find_element(driver,shopping_bag).click()          # 点击“购物袋”
        find_element(driver,immediate_settlement).click()  # 点击“立即结算”

        title = driver.title                       # 获取当前title

        if title == "订单":
            print("测试成功！")
        else:
            self.assertEqual(title, "登录", "测试失败！")

            find_element(driver,phone_number).send_keys("18262620731")   # 输入手机号码
            find_element(driver,password).send_keys("zxcvbnm123")        # 输入密码
            find_element(driver,login).click()                           # 点击“登录”
            find_element(driver,shopping_bag).click()                    # 点击“购物袋”
            find_element(driver,immediate_settlement).click()            # 点击“立即结算”

            title = driver.title                                 # 获取当前title

            self.assertEqual(title, "订单", "测试失败！")
            print("测试成功！")

        driver.quit()

if __name__ == "__main__":
    unittest.main()


"""
            查找单个元素
                参数：locator=("id", "123")
                类型：
                ID = "id"
                XPATH = "xpath"
                LINK_TEXT = "link text"
                PARTIAL_LINK_TEXT = "partial link text"
                NAME = "name"
                TAG_NAME = "tag name"
                CLASS_NAME = "class name"
                CSS_SELECTOR = "css selector"
"""