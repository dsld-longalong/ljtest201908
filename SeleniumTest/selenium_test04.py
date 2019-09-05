"""
    切换窗口句柄
"""
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://132.232.44.158:8080/morning/")

driver.find_element_by_link_text("苹果6s").click()

time.sleep(3)
# 查看所有窗口句柄
print("所有窗口的句柄:{}".format(driver.window_handles))
print("当前窗口的句柄:{}".format(driver.current_window_handle))

# 切换到最后一个窗口的句柄
driver.switch_to_window(driver.window_handles[-1])
driver.find_element_by_xpath('//*[@id="form"]/div[2]/label/a/p')

print("切换之后的窗口句柄:{}".format(driver.current_window_handle))

driver.quit()