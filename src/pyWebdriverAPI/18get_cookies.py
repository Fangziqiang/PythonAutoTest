#coding=utf-8
#webdriver操作cookie的方法有：
# get_cookies() 获得所有cookie信息
# get_cookie(name)  返回特定name的cookie信息
# add_cookie(cookie_dict)添加cookie，必须有name和value值
# delete_cookie(name) 删除特定（部分）的cookie信息
# delete_all_cookies() 删除所有cookie信息
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

#获得cookie信息
cookie = driver.get_cookies()

#打印cookie信息
print cookie

driver.quit()