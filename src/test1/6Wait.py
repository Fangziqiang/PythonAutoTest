#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

element=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id("kw"))
element.send_keys("selenium")

#添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()

#添加固定