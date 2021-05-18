import time
from selenium import webdriver

driver = webdriver.Firefox()

# 设置隐性等待, 单位是 s
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

elem = driver.find_element_by_id('kw')
elem.send_keys('浩仔')
elem.submit()

# 强制等待
# time.sleep(3)
# 隐性等待：只能用来等待元素出现。
# 启动浏览器只需要设置一次。

print(driver.title)
# elem = driver.find_element_by_id('kw')
driver.quit()

# 显性等待。
# xpath
# 三种
