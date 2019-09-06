"""
    二次封装：以方法的形式存放
"""
"""
    二次封装
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def find_element(locator, driver, timeout=10):
    """
        动态查找元素的二次封装
    """
    try:
        e = WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))
        return e
    except:
        return None

def click(locator, driver):
    """
        点击元素
    """
    e = find_element(locator, driver)
    e.click()


def input(locator, driver, content):
    """
        输入
    """
    e = find_element(locator, driver)
    e.send_keys(content)

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.baidu.com/")

# search_input_locator = ("xpath", '//*[@id="kw"]')
# e = find_element(search_input_locator, driver)
# e.send_keys("1235456")

# search_button = ("link text", "新闻")
# click(search_button, driver)            # 点击效果

search_input = ("id", "kw")
input(search_input, driver, "selenium！")