# //span[text()='设置']

import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(4)
driver.get('http://www.baidu.com')

# 找到要移动到的元素
setting = driver.find_element('xpath', "//span[text()='设置']")

# 鼠标悬停， move_to_element
ac = ActionChains(driver)
ac.move_to_element(setting).perform()

time.sleep(3)

# 找到高级搜索
adv_setting = driver.find_element('xpath', "//a[text()='高级搜索']")
adv_setting.click()
# ac.click(adv_setting).perform()

time.sleep(2)

# 链式调用
ac.move_to_element(setting).click(adv_setting).drag_and_drop().context_click().perform()




