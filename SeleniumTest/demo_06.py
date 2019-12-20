'''
购物车结算测试用例:
1、如果没有登录，那么会跳转到登录页面，先登录之后再去结算。
2、如果是已经登录的了呢；最后的判断结果一定是订单结算页面。
'''
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./drivers/chromedriver") 
driver.maximize_window() 
driver.get("http://118.24.29.59:8080") 

try:
    driver.find_element_by_xpath('//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img').click() # 点击“水晶冰菜”图片
    driver.find_element_by_id("J_mer_saleTag").click() # 点击“加入购物袋”
    # driver.refresh() # 刷新页面，否则无法点击“购物袋”
    driver.find_element_by_xpath('//*[@id="J_header_cart"]/div[1]/a[1]').click() # 点击“购物袋”
    driver.find_element_by_xpath('//*[@id="J_cart_bar"]/div[1]/a').click() # 点击立即结算
    title = driver.title # 获取当前title

    # 判断当前title是否等于“订单”
    if title == "订单": 
        print("测试成功！")
    elif title == "登录":
        driver.find_element_by_id("username").send_keys("18262620731") # 输入手机号码
        driver.find_element_by_id("password").send_keys("zxcvbnm123") # 输入密码
        driver.find_element_by_id("btnLogin").click() #点击“登录”
        driver.find_element_by_xpath('//*[@id="J_header_cart"]/div[1]/a[1]').click() # 点击“购物袋”
        driver.find_element_by_xpath('//*[@id="J_cart_bar"]/div[1]/a').click() # 点击立即结算
        title = driver.title # 获取当前title
        # 判断当前title是否等于“订单”
        if title == "订单":
            print("测试成功！")
        else:
            print("测试失败！")
    else:
        print("测试失败！")
except:
    print("测试失败！")
    
driver.quit()