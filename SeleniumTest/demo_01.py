'''自动打开网址'''
def qurey(res):
    from selenium import webdriver
    import time
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")   #对谷歌浏览器进行实例化
    time.sleep(3)
    driver.get("https://www.baidu.com")  #在浏览器中输入网址  
    time.sleep(3)
    # <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">

    driver.find_element_by_id("kw").send_keys(res)   #通过元素的id来定位
    # driver.find_element_by_name("wd").send_keys(res)  #通过元素的name来定位
    # driver.find_element_by_class_name("s_ipt").send_keys(res)    #通过元素的class_name来定位
    # driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys(res)    #通过元素的xpath来定位
    # driver.find_element_by_css_selector("input#kw.s_ipt").send_keys(res)  #通过元素的css_selector来定位
    # driver.find_element_by_link_text("新闻").click()    #通过超链接的文本来定位    看demo13.py
    # driver.find_element_by_partial_link_text("老英雄的双手").click()    #通过超链接的部分文本来定位    看demo13.py
    # driver.find_element_by_tag_name   #通过tag_name来定位

    # driver.maximize_window()    #窗口最大化
    # driver.minimize_window()    #窗口最小化

    # driver.execute()    #可以写入一些JS的代码，可在浏览器中执行（JavaScript代码）

    # winlist = driver.window_handles   #获取所有句柄
    # print(winlist)
    # windowname = driver.current_window_handle   #获取当前句柄
    # print("第一个窗口是：",windowname)
    # driver.switch_to.window(winlist[1])     #切换句柄
    # windowname = driver.current_window_handle   #获取当前句柄
    # print("第二个窗口是：",windowname)
    time.sleep(3)
    # <input type="submit" id="su" value="百度一下" class="bg s_btn">

    driver.find_element_by_id("su").click() #点击 百度一下 按钮
    time.sleep(5)
    title = driver.title    #获取title
    if "{}_百度搜索".format(res) == title:  
        print("测试通过，搜索成功！")
    else:
        print("测试失败！")
    driver.quit()   #退出浏览器
res = input("请输入所查询的内容：")
qurey(res)