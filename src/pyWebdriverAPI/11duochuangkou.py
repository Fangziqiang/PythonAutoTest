#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#获得当前窗口
nowhandle=driver.current_window_handle

#打开注册新窗口
#driver.find_element_by_name("tj_reg").click()
driver.find_element_by_link_text(u"登录").click()
#通过二次定位找到用户名输入框
time.sleep(3)
div=driver.find_element_by_class_name("tang-content").find_element_by_link_text(u"立即注册")
div.click()
#获得所有窗口
allhandles=driver.window_handles

#循环判断窗口是否为当前窗口
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to_window(handle)
        print 'now register window!'
    #切换到邮箱注册标签
#     driver.find_element_by_id("mailRegTab").click()
#     time.sleep(5)
#     driver.close()
#回到原来的窗口
driver.switch_to_window(nowhandle)

driver.find_element_by_id("kw").send_keys(u"注册成功")
time.sleep(3)
#driver.quit()
    
    
    
    