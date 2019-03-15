#coding=utf-8
from selenium import webdriver
import selenium.common.exceptions

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

try:
#找不到id=kwsss时将会进入except执行
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
except selenium.common.exceptions.NoSuchElementException, msg:
    driver.get_screenshot_as_file("picture1.jpg")
    print msg
driver.quit()