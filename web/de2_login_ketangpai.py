import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get('https://www.ketangpai.com/#/login')
driver.maximize_window()
# time.sleep(3)
# driver.find_element("xpath", '//div/input[@autocomplete="on"]').send_keys("15195989321")
# driver.find_element("xpath", '//div/input[@placeholder="请输入密码"]').send_keys("Beyondqn01")
wait = WebDriverWait(driver, 10)
username = wait.until(
    expected_conditions.visibility_of_element_located(["xpath", '//div/input[@autocomplete="on"]'])).send_keys(
    '15195989321')
password = wait.until(
    expected_conditions.visibility_of_element_located(["xpath", '//div/input[@placeholder="请输入密码"]'])).send_keys(
    'Beyondqn01')

setting = driver.find_element('xpath', '//div/button[@class="el-button el-button--primary"]')

# 元素定位相互覆盖时（js语句执行）
driver.execute_script("arguments[0].click();", setting)
