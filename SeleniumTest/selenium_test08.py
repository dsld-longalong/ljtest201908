"""
    鼠标事件
        - 悬停事件
        - 单击
        - 右键
        - 双击
        - 拖拽
"""
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.baidu.com/")

# 单击：click()

# 悬停
more_product = driver.find_element_by_link_text("更多产品")
ActionChains(driver).move_to_element(more_product).perform()    # 最后一定要去调用perform方法
driver.find_element_by_link_text("糯米").click()

# 双击
# news = driver.find_element_by_link_text("新闻")
# ActionChains(driver).double_click(news).perform()

# 右键
# news = driver.find_element_by_link_text("新闻")
# ActionChains(driver).context_click(news).perform()

# time.sleep(3)
# 拖拽
# s = driver.find_element_by_id("kw")
# s.send_keys("asdfasd")
# img = driver.find_element_by_xpath('//*[@id="result_logo"]/img[1]')
# ActionChains(driver).drag_and_drop(img, s).perform()

time.sleep(3)
driver.quit()
