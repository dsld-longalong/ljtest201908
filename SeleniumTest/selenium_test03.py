
import time
from selenium import webdriver

# 1. 打开浏览器
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()    # 把浏览器最大化

# 2. 访问百度首页
driver.get("https://www.baidu.com/")
# 3. 在首页的搜索框输入黄晓明
e = driver.find_element_by_xpath('//*[@id="kw"]')
e.send_keys("黄晓明")
# 4. 点击百度一下按钮
a = driver.find_element_by_xpath('//*[@id="su"]')
a.click()

time.sleep(1)
c = driver.find_element_by_xpath('//*[@id="1"]/h3/a')

# 获取文本值
print(c.text)

e.clear()


time.sleep(3)

driver.quit()