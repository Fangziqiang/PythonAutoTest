#coding=gbk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Ie()

browser.get('http://www.baidu.com')

elem = browser.find_element_by_name('wd')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
browser.find_element_by_name('wd');