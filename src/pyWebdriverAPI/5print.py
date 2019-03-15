#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
#driver = webdriver.Ie()
driver = webdriver.Firefox()

driver.get("http://email.163.com/")
#登录
driver.find_element_by_id("userNameIpt").clear()
driver.find_element_by_id("userNameIpt").send_keys("17610831883")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("021131.ai")
driver.find_element_by_id("btnSubmit").click()
#time.sleep(3)
#获得前面 title，打印
title = driver.title
print title
#获得前面 URL，打印
now_url = driver.current_url
print now_url
#获得登录成功的用户，打印
#driver.implicitly_wait(3)
#WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
#WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
element=WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_id("spnUid"))
now_user=driver.find_element_by_id("spnUid").text
print now_user
driver.quit()