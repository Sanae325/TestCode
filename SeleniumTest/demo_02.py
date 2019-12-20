from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="./drivers/chromedriver")   #对谷歌浏览器进行实例化
time.sleep(3)
driver.get("https://www.baidu.com")  #在浏览器中输入网址
time.sleep(3)
driver.find_element_by_link_text("新闻").click()    #通过超链接的文本来定位
time.sleep(3)
driver.find_element_by_partial_link_text("老英雄的双手").click()    #通过超链接的部分文本来定位
time.sleep(5)
driver.quit()   #退出浏览器