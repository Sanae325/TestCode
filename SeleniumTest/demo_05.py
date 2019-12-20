'''
加入购物车的测试用例：
首页选择水晶冰菜 -> 跳转到商品的详情页面 -> 加入购物车 -> 再返回到购物车里面，去判断水晶冰菜有没有加入到购车里面
'''
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./drivers/chromedriver")  
driver.maximize_window() 
driver.get("http://118.24.29.59:8080") 

driver.find_element_by_id("J_header_lnkLogin").click()
driver.find_element_by_id("username").send_keys("18262620731")
driver.find_element_by_id("password").send_keys("zxcvbnm123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_xpath('//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img').click()
driver.find_element_by_id("J_mer_saleTag").click()
driver.refresh()
driver.find_element_by_xpath('//*[@id="J_header_cart"]/div[1]/a[1]').click()
text = driver.find_element_by_link_text("水晶冰菜").text

if text == "水晶冰菜":
    print("测试成功!")
else:
    print("测试失败!")

driver.quit()