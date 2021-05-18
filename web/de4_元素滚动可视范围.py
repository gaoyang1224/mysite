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
el = driver.find_element('xpath', "//h2[contains(text(),'友情链接')]")
el.location_once_scrolled_into_view
