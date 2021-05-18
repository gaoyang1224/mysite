import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.huya.com/')
time.sleep(3)
el = driver.find_element('id', 'search-bar-input')
driver.execute_script('arguments[0].placeholder="UZI"', el)
sub = driver.find_element('xpath', '//button')
driver.execute_script('arguments[0].click()', sub)

handler = driver.window_handles[-1]
driver.switch_to.window(handler)

print(driver.title)

setting = driver.find_element('id', 'hy-nav-category')
ac = ActionChains(driver)
ac.move_to_element(setting).perform()

driver.find_element("xpath", "//a[text()='交友']").click()
