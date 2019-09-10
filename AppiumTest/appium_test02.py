# 1.导入appium
import time
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


# 点击 click

# 按键
# driver.press_keycode(4)

# 返回
driver.back()

# 滑动
for i in range(10):
    driver.swipe(100, 800, 800, 800)
    time.sleep(1)