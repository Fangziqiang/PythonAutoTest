#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import xml.dom.minidom

"'读取xml配置信息'"
#引入xml文件
dom=xml.dom.minidom.parse('info.xml')
root=dom.documentElement

#获取url，使用方法：获得<url></url>标签对之间的数据
url_tag=dom.getElementsByTagName('url')
url=url_tag[0].firstChild.data
print url

#获取登录的用户名密码,获得username、passwd标签的属性所对应的值
userinfo=dom.getElementsByTagName('login')
username = userinfo[0].getAttribute("username")
passwd = userinfo[0].getAttribute("passwd")
print username,passwd

"脚本引用xml配置信息"
driver = webdriver.Firefox()
driver.get(url)

driver.maximize_window()
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()





