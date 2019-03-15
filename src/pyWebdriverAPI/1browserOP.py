#coding=utf-8
#操作浏览器

#  %s:表示输出的类型为字符串
#  %d:表示输出的类型为整型数字
#  如果我们不确定变量类型的话可以使用%r，它的含义是“不管什么都打印出来”。
from selenium import webdriver
import time
first_url='http://www.baidu.com'
second_url='http://news.baidu.com'

#访问百度首页
driver = webdriver.Ie()
print "now access %s" %(first_url)
driver.get(first_url)

#访问新闻页面
print "now acess %s" %(second_url)
driver.get(second_url)

#浏览器后退
print "back to %s"%(first_url)
driver.back()

#浏览器前进
print "foward to %s"%(second_url)
driver.forward()

#浏览器最大化
print "浏览器最大化"
driver.maximize_window() 

#设置浏览器宽高
print "设置浏览器宽480、高800显示"
driver.set_window_size(480, 800)

#控制浏览器前进、后退


driver.quit()