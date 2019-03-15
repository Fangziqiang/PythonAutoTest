#coding=utf-8
#webdriver中处理Javascript所生成的alert、confirm以及prompt是很简单的，
#具体思路是使用swich_to_alert()方法定位到alert/confirm/prompt，然后使用
#text/accept/dismiss/send_keys按需进行操作
#text: 返回alert/confirm/prompt中的文字信息
#accept： 点击确定按钮
#dismiss：点击取消按钮，如果有的话
#send_keys: 输入值，这个alert/confirm没有对话框就不能用了，不然会报错
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#点击打开搜索设置
driver.implicitly_wait(5)
driver.find_element_by_class_name("tj_settingicon").click()
#driver.find_element_by_link_text(u"设置").click()
time.sleep(3)
driver.find_element_by_link_text(u"搜索设置").click()
#driver.find_element_by_class_name("setpref").click()
#点击保存设置
time.sleep(1)
driver.find_element_by_link_text(u"保存设置").click()
#driver.find_element_by_xpath("//div[@id='gxszButton']/input").click()

#获取网页上的警告信息
alert=driver.switch_to_alert()
texts=driver.switch_to_alert().text
#接收警告信息
alert.accept()
print texts
driver.quit()








