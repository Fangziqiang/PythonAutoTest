#coding=utf-8

from selenium import webdriver
import os
import file_path

driver=webdriver.Firefox()
driver.get(file_path.checkbox_path)
print file_path.checkbox_path

#选择页面上所有tag_name为input的元素
inputs=driver.find_elements_by_tag_name("input")

#从中过滤出type为checkbox的元素，单击勾选
for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
        
#driver.quit()