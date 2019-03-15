#coding= utf-8
#<input type="checkbox" data-node="594434499" data-convert="1" data-type="file">
#<input type="checkbox" data-node="594434498" data-convert="1" data-type="file">
#<input type="checkbox" data-node="594434493" data-convert="1" data-type="file">
#<input type="checkbox" data-node="594434497" data-convert="1" data-type="file">

from selenium import webdriver
driver = webdriver.Firefox()
#选择页面上所有的tag_name为input的元素
inputs =driver.find_element_by_tag_name('input')
#循环遍历出data-node为594434493的元素，单击勾选
for input in inputs:
    if input.get_attribute('data-node')=='594434493':
        input.click()