from selenium import webdriver


def test_start_selenium():
    driver = webdriver.Chrome()
    url = "https://www.douban.com"
    driver.get(url)

    input_el = driver.find_element_by_name("q")
    input_el.send_keys("老友记")
    input_el.submit()

    # 断言
    actual = driver.title
    driver.quit()
    assert actual == '搜索: 老友记'


# 执行pytest test_start_selenium.py
# 生成报告pytest --html=output.html
