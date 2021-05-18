import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get('https://www.12306.cn/index/')
driver.maximize_window()
time.sleep(3)
el = driver.find_element('id', 'train_date')
driver.execute_script("arguments[0].value='2021-03-30';arguments[0].readonly='false'", el)