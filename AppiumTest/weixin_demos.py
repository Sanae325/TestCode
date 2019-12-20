# 1.导入appium的webdriver
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def get_driver(pv="5.1.1", dn="vivo x6plus d", ap="com.tencent.mm", aa=".ui.LauncherUI"):
    """
        传入对应的参数去打开手机app,并且去返回这个driver对象
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'            # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = pv                # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = dn                     # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = ap                     # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['appActivity'] = aa                    # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['unicodeKeyboard'] = True              # 为了支持中文
    desired_caps['resetKeyboard'] = True                # 设置成appium自带的键盘

    # 解锁手机并且去打开app
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

def find_element(driver, locator):
    """
        传入locator = ("id", "id->value")
        id: "id"
        xpath: "xpath"
        accessibility_id: "accessibility id"
        android_uiautomator: "-android uiautomator"
    """
    return WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))



if __name__ == "__main__":
    driver = get_driver()

    register = ("-android uiautomator", 'new UiSelector().text("登录")')
    phone = ("xpath", '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')
    next_step = ("-android uiautomator", 'new UiSelector().text("下一步")')
    password = ("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')
    login = ("-android uiautomator", 'new UiSelector().text("登录")')
    no = ("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[1]')

    find_element(driver, register).click()
    find_element(driver, phone).set_value("18262620731")
    find_element(driver, next_step).click()
    find_element(driver, password).set_value("zxcvbnm123")
    find_element(driver, login).click()
    find_element(driver, no).click()
