#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#定位登录按钮，方法一：报错
#element=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_name("tj_login"))
#element.click()
#方法二：没有问题
driver.find_element_by_link_text(u"登录").click()
#方法三：报错
#driver.implicitly_wait(3)
#driver.find_element_by_name('tj_login').click()
#通过二次定位找到用户名输入框
div=driver.find_element_by_class_name("tang-content").find_element_by_name("userName")
div.send_keys(u"听风AIF")

#输入登录密码
driver.find_element_by_name("password").send_keys("159753ai")

#点击登录
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

driver.quit()