#coding=utf-8

from selenium import webdriver
import time
import os

file_path='file:\\\G:\\eclipse-workspace\\1111\\src\\htmlfiles\\drop_down.html'
driver=webdriver.Firefox()
driver.get(file_path)
time.sleep(2)

#先定位到下拉框
m=driver.find_element_by_id("ShippingMethod")
#再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)

#driver.quit()
