def qurey(res):   
    from selenium import webdriver
    import time
    def find(driver,timeout,locator):
        from selenium.webdriver.support.ui import WebDriverWait
        element = WebDriverWait(driver,timeout).until(lambda s: s.find_element(*locator))
        return element

    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")  
    driver.maximize_window()
    driver.get("https://www.baidu.com")  

    search_input = ("id","kw")
    search_button = ("id","su")
    find(driver,10,search_input).send_keys(res)
    find(driver,10,search_button).click()
    
    time.sleep(1)
    title = driver.title

    if "{}_百度搜索".format(res) == title:  
        print("测试通过，搜索成功！")
    else:
        print("测试失败！")
    driver.quit()  

res = input("请输入所查询的内容：")
qurey(res)



# from selenium import webdriver

# # 动态查找封装成一个方法
# # 二次封装
# def find(driver,timeout,locator):
#     from selenium.webdriver.support.ui import WebDriverWait # 导入动态查找需要的第三方包
#     element = WebDriverWait(driver,timeout).until(lambda s: s.find_element(*locator)) # 实现元素的动态定位
#     return element # 返回元素

# driver = webdriver.Chrome(executable_path="./drivers/chromedriver")  
# driver.maximize_window()
# driver.get("https://www.baidu.com")  

# search_input = ("id","kw")
# search_button = ("id","su")
# find(driver,10,search_input).send_keys(111)
# find(driver,10,search_button).click()

# title = driver.title

# if "111_百度搜索" == title:  
#     print("测试通过，搜索成功！")
# else:
#     print("测试失败！")

# driver.quit()  
    
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"