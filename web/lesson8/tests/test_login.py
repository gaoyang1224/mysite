import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    """启动浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def login():
    """登录过程"""



class TestLogin:

    def test_without_username_and_password(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://v4.ketangpai.com/User/login.html")
        driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/a[1]').click()
        expected = '账号不能为空'
        actual = driver.find_element_by_class_name('error-tips')
        assert expected == actual.text


    def test_without_username(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://v4.ketangpai.com/User/login.html")
        driver.find_element('name', 'account').send_keys('')
        driver.find_element('name', 'pass').send_keys('Beyondqn01')
        driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/a[1]').click()
        expected = '账号不能为空'
        actual = driver.find_element_by_class_name('error-tips')
        assert expected == actual.text


    def test_login_success(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://v4.ketangpai.com/User/login.html")
        driver.find_element('name', 'account').send_keys('15195989321')
        driver.find_element('name', 'pass').send_keys('Beyondqn01')
        driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/a[1]').click()
        time.sleep(3)
        assert driver.current_url == 'https://v4.ketangpai.com/Main/index.html'
        user_elen = driver.find_element('xpath', "//img[@class='avatar']")
        assert user_elen.get_attribute('title') == 'GY'