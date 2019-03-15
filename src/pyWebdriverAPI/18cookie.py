#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

#向cookie的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbbb'})

#遍历cookies中的name和value信息打印
for cookie in driver.get_cookies():
    print "%s->%s" %(cookie['name'],cookie['value'])
    
#删除一个特定的cookie(name=key-aaaaaaa的cookie)
driver.delete_cookie("key-aaaaaaa")
for cookie in driver.get_cookies():
    print "%s->%s" %(cookie['name'],cookie['value'])
#删除所有cookie
driver.delete_all_cookies()

time.sleep(2)
driver.close()

