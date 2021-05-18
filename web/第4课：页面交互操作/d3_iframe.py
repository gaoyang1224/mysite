"""iframe"""

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=html_select')

# 如果想找一个 iframe 当中的元素，不能直接查找，而是先要进入 iframe 当中，
# 提供iframe 的标识： index, name, iframe Webelement

# 通过 WebElement 切换
iframe = driver.find_element('id', 'iframeResult')
driver.switch_to.frame(iframe)

# 通过 name 属性切换
driver.switch_to.frame('iframeResult')

# 通过索引切换
driver.switch_to.frame(0)

elem = driver.find_element('xpath', '//select')

# 退回主页面
driver.switch_to.default_content()

# 退回父级iframe
# driver.switch_to.parent_frame()

print(elem)