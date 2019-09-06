"""
    键盘事件
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("实时路况打飞机啊塑料袋解")
driver.find_element_by_id("kw").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("kw").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("kw").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("kw").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("kw").send_keys(Keys.BACKSPACE)

driver.find_element_by_id("kw").send_keys(Keys.F5)

time.sleep(3)

driver.quit()