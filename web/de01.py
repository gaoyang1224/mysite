import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

driver.implicitly_wait(10)

driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("Apink")

# 显性等待
wait = WebDriverWait(driver, 10)
# 等待元素加载
el = wait.until(expected_conditions.presence_of_element_located(['id', 'kw']))
# 等待元素可见
#el = wait.until(expected_conditions.visibility_of_element_located(['id', 'kw']))
# 等待元素可以被点击
#el = wait.until(expected_conditions.element_to_be_clickable(['id', 'kw']))
el.send_keys('Apink')
driver.find_element_by_xpath("//input[@id='su']").click()

driver.find_element_by_xpath("//h3[@class='t c-gap-bottom-small']//a").click()

# 切换
handler =driver.window_handles[-1]
driver.switch_to.window(handler)

time.sleep(3)
print(driver.title)

# 鼠标悬停
setting = driver.find_element("xpath", "//a[text()='首页']")
ac = ActionChains(driver)
ac.move_to_element(setting).perform()

driver.find_element('xpath',"//a[text()='历史上的今天']").click()
#driver.quit()
