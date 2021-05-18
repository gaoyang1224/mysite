from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(4)
driver.get('file:///D:/classes/web_auto_testing/%E7%AC%AC4%E8%AF%BE%EF%BC%9A%E9%A1%B5%E9%9D%A2%E4%BA%A4%E4%BA%92%E6%93%8D%E4%BD%9C/alert_demo.html')

h2 = driver.find_element('xpath', '//h2')
h2.click()

# 切换到 alert, 点击确定, 没有括号，也不需要传参数， 全局只有一个。
my_alert = driver.switch_to.alert
# 确定
my_alert.accept()
# # 取消
# my_alert.dismiss()

driver.find_element('xpath', '//h2')