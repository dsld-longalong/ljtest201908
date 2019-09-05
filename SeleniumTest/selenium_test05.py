"""
    iframe
"""
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://passport2.eastmoney.com/pub/login")


# 1. 切换iframe
ifreme = driver.find_element_by_id("frame_login")
driver.switch_to_frame(ifreme)

time.sleep(3)
driver.find_element_by_id("txt_account").send_keys("13000000001")
time.sleep(3)

# 2. 切换回大网页
driver.switch_to_default_content()

driver.find_element_by_link_text("东方财富网免费版").click()


driver.quit()