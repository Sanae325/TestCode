from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="./drivers/chromedriver")   #对谷歌浏览器进行实例化
driver.maximize_window() 
time.sleep(2)
driver.get("http://114.116.106.156/show-how/common/login.jsp")  #在浏览器中输入网址
time.sleep(2)
driver.find_element_by_id('username').send_keys("test007")
time.sleep(2)
driver.find_element_by_id('password').send_keys("1")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="userForm"]/div[1]/div[4]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="missionTableBody"]/tr[1]/td[1]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="box01"]/div[1]/div[3]').click() # 点击差号，关闭当前窗口
time.sleep(2)
driver.find_element_by_xpath('//*[@id="leftContent"]/div[2]/div[1]/div/div[1]/a').click()
time.sleep(2)
driver.quit()
