#coding=utf-8
from counter import counter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.baidu.com')

elem = browser.find_element_by_id('kw')  # Find the search box
elem.send_keys('百度一下' + Keys.RETURN)
import sys
print sys.getdefaultencoding()
d=counter
d.substract(10000000, 5000000)

#browser.quit()