import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()

# 设置隐性等待, 单位是 s
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

elem = driver.find_element('id', 'kw')

elem.send_keys('浩仔')
elem.submit()

# 查找京东
driver.find_element_by_link_text('京东').click()
# 等待新页面出现
time.sleep(5)

# 切换
# 窗口的句柄传进去。
# 现在打开的所有的窗口句柄
# print(driver.window_handles)
# # 打印现在的窗口句柄
# print(driver.current_window_handle)
handle = driver.window_handles[-1]  #"41"
driver.switch_to.window(handle)

time.sleep(2)
# print(driver.current_window_handle)
# 京东
print(driver.title)



