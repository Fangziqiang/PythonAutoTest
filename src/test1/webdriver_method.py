# -*- coding: utf-8 -*- #
import time #调入time函数
from selenium import webdriver
browser=webdriver.Ie()
browser.get("http://www.baidu.com")
#ͨ通过id定位
browser.find_element_by_id("kw").send_keys("1123")

#ͨ通过name定位
browser.find_element_by_name("wd").send_keys("selenium")
 
#ͨ通过tag_name定位
browser.find_element_by_tag_name("input").send_keys("selenium")
 
#通过class name定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
 
#通过CSS定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
 
#通过xpath定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

######################################################
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()








