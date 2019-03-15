#coding = utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://192.168.20.102:8080/mbcp/ssoLogin.jsp")
cookies=driver.get_cookies()

for cookie in driver.get_cookies():
    print "%s->%s" %(cookie['name'],cookie['value'])

#driver.add_cookie(cookie_dict)
#driver.add_cookie(cookie_dict)
#driver.get("http://192.168.20.102:8080/mbcp/")