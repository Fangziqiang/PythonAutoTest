#coding=utf-8

from selenium import webdriver
import os
import file_path

driver=webdriver.Firefox()
driver.get(file_path.checkbox_path)

checkboxes=driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
    
#打印当前页面上type为checkbox的个数
print len(driver.find_elements_by_css_selector('input[type=checkbox]'))

#把页面最后一个checkbox的勾去掉,用于删除指定们位置的元素，pop()为空默认选择最一个元素
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
