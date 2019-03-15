#coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://")

#登录系统
driver.find_element_by_id("id_").clear()
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("").click()
sleep(2)

#获取所有分页的数量，并打印
total_page=len(driver.find_element_by_tag_name("select").find_element_by_tag_name("option"))
print "total page is %s" %(total_page)
sleep(3)

#再次获取所有分页，并执行循环翻页操作
pages=driver.find_element_by_tag_name("select").find_element_by_tag_name("option")

for page in pages:
    page.click()
    sleep(2)
    
sleep(3)
driver.quit()

    



