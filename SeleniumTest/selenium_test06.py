"""
    动态查找，固定的写法
"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.baidu.com/")

# 动态查找元素

# id
# search_input_locator = ("id", "kw")
# search_input = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input_locator))
# search_input.send_keys("test")

# name
# search_input_locator = ("name", "wd")
# search_input = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input_locator))
# search_input.send_keys("test")

# xpath
# search_input_locator = ("xpath", '//*[@id="kw"]')
# search_input = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input_locator))
# search_input.send_keys("test")

# css_selector
# search_input_locator = ("css selector", '#kw')
# search_input = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input_locator))
# search_input.send_keys("test")

# class_name
# search_input_locator = ("class name", "s_ipt")
# search_input = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input_locator))
# search_input.send_keys("test")

# link_text
# search_input_locator = ("link text", "hao123")
# search_input = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input_locator))
# search_input.click()

# partial_link_text
# search_input_locator = ("partial link text", "hao")
# search_input = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input_locator))
# search_input.click()

# tag_name
e_locator = ("tag name", "input")
e = WebDriverWait(driver, 10).until(lambda s: s.find_element(*e_locator))
print(e)

time.sleep(1)
driver.quit()

