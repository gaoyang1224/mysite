import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    """启动浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def login(driver, username, password):
    """登录过程"""
    driver.find_element('name', 'account').send_keys(username)
    driver.find_element('name', 'pass').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/a[1]').click()


def load(driver, url):
    driver.get(url)

def clear(driver):
    driver.find_element('name', 'account').clear()
    driver.find_element('name', 'pass').clear()

class login:
    def __init__(self,driver):
        self.driver = driver

    def login(self, username, password):
        """登录过程"""
        self.driver.find_element('name', 'account').send_keys(username)
        self.driver.find_element('name', 'pass').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/a[1]').click()

    def load(self, url):
        self.driver.get(url)

    def clear(self):
        self.driver.find_element('name', 'account').clear()
        self.driver.find_element('name', 'pass').clear()



class TestLogin:

    def test_without_username_and_password(self):
        driver = get_driver()
        driver.get("https://v4.ketangpai.com/User/login.html")
        login(driver, "", "")
        expected = '账号不能为空'
        actual = driver.find_element_by_class_name('error-tips')
        assert expected == actual.text

    def test_without_username(self):
        driver = get_driver()
        driver.get("https://v4.ketangpai.com/User/login.html")
        login(driver, "", "Beyondqn01")
        expected = '账号不能为空'
        actual = driver.find_element_by_class_name('error-tips')
        assert expected == actual.text

    def test_login_success(self):
        driver = get_driver()
        driver.get("https://v4.ketangpai.com/User/login.html")
        login(driver, "15195989321", "Beyondqn01")
        time.sleep(3)
        assert driver.current_url == 'https://v4.ketangpai.com/Main/index.html'
        user_elen = driver.find_element('xpath', "//img[@class='avatar']")
        assert user_elen.get_attribute('title') == 'GY'
