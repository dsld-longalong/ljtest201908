"""
    selenium的简单demo
"""
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.baidu.com/")

# id
# search_input = driver.find_element_by_id("kw")
# search_input.send_keys("12345")

# name
# search_input = driver.find_element_by_name("wd")
# search_input.send_keys("12345")

# xpath
# search_input = driver.find_element_by_xpath('//*[@id="kw"]') # 注意外单内双
# search_input.send_keys("12345")

# css_selector
# search_input = driver.find_element_by_css_selector('#kw') # 注意外单内双
# search_input.send_keys("12345")

# class_name
# class_name：元素的classname可能会重复
# search_input = driver.find_element_by_class_name("s_ipt")
# search_input.send_keys("12345")

# link_text
# hao123 = driver.find_element_by_link_text("hao123")
# hao123.click()

# partial_link_text
# hao123 = driver.find_element_by_partial_link_text("hao")
# hao123.click()

# tag_name
# e = driver.find_element_by_tag_name("input")
# e.send_keys("1234")


time.sleep(3)
driver.quit()