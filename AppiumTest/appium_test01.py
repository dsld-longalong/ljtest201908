# 1.导入appium
from appium import webdriver

# 2.去打开app并且获取driver对象（app的操作对象）
# 2.1获取手机和app的信息
app_info = {}
app_info["platformName"] = "Android"        # 打开什么平台的app，固定的
app_info["platformVersion"] = "5.1.1"       # 安卓系统的版本号：adb shell getprop ro.build.version.release
app_info["deviceName"] = "vivo x6plus d"    # 安卓设备的型号：adb shell getprop ro.product.model
app_info["appPackage"] = "io.appium.android.apis"   # 软件的包名：adb shell dumpsys activity | findstr "mFocusedActivity"
app_info["appActivity"] = ".ApiDemos"       # 软件启动页面的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
app_info['unicodeKeyboard'] = True          # 为了支持中文
app_info['resetKeyboard'] = True            # 设置成appium自带的键盘

# 2.2打开app并且获取driver对象（app的操作对象）
driver = webdriver.Remote("http://localhost:4723/wd/hub", app_info)

# 定位方式1：Accessibility id
# e = driver.find_element_by_accessibility_id("Accessibility")
# # 点击
# e.click()

# # 定位方式2：xpath
# e1 = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility Node Provider"]')
# # 获取文本值
# print(e1.text)

# # 定位方式3：by_id > resource id
# e2 = driver.find_element_by_id("android:id/text1")
# e2.click()

# 定位方式4：text
driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("Search")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("Invoke Search")').click()
e3 = driver.find_element_by_id('io.appium.android.apis:id/txt_query_prefill')
e3.send_keys("黄晓明")          # 输入中文

# 清除输入的信息
e3.clear()

# 快速的输入，不支持中文
driver.set_value(e3, "xiaoming!")

# 关掉
driver.quit()