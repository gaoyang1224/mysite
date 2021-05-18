import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(4)
driver.get('file:///D:/classes/web_auto_testing/%E7%AC%AC4%E8%AF%BE%EF%BC%9A%E9%A1%B5%E9%9D%A2%E4%BA%A4%E4%BA%92%E6%93%8D%E4%BD%9C/alert_demo.html')


# 复杂版：
# 初始化 ActionChains: 动作链条，
action = ActionChains(driver)
# 定位一个元素
h2 = driver.find_element('xpath', '//h2')
# click 操作
action.click(h2).perform()


time.sleep(5)

# 简单
# h2 = driver.find_element('xpath', '//h2')
# h2.click()





