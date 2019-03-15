#coding=utf-8

#webdriver提供了execute_script()接口用来调用js代码,执行js一般有两种场景，
#一种是在页面上直接执行JS
#另一种是在某个已经定位的元素上执行JS

#execute_script(script,*args)
#在当前窗口/框架 同步执行javaScript


from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = 'file:///G://eclipse-workspace//1111//src//htmlfiles//js.html'
driver.get(file_path)

if 'HTTP_PROXY' in os.environ:del os.environ['HTTP_PROXY']

########通过JS隐藏选中的元素########
#隐藏文字信息
text = driver.find_element_by_id("tooltip")
print (text.is_displayed())
time.sleep(5)
myjs = 'document.getElementById("tooltip").style.display="none";'
driver.execute_script(myjs)

print "Hide element"
print (text.is_displayed())

#隐藏按钮：
button = driver.find_element_by_class_name('btn')
myjs1 = 'getClass("a","btn")[0].style.display="none";'
driver.execute_script(myjs1)
time.sleep(5)

driver.quit()




