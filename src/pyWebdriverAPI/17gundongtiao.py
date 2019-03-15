#coding=utf-8

#一般用到操作滚动条的会两个场景：
# 注册时的法律条文的阅读，判断用户是否阅读完成的标准是：滚动条是否拉到最下方。
# 要操作的页面元素不在视觉范围，无法进行操作，需要拖动滚动条
#用于标识滚动条位置的代码
#    <body onload= "document.body.scrollTop=0 ">
#    <body onload= "document.body.scrollTop=100000 ">
# document.body.srollTop  网页被卷去的高
# scrollTop：设置或获取位于对象最顶端和窗口中可见内容的最顶端之间的距离
#    100000 的值是指的像素点，只要我们设置的告诉大于整个页面的高度，就可以把浏览器拖动到最底
#    部。如果滚动条在最上方的话，scrollTop=0 ，那么要想使用滚动条在最可下方，可以 scrollTop=100000
#    （大于整个页面高度） ，这样就可以使滚动条在最下方。

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
 
#将页面滚动条拖到顶部
js2="var q=document.documentElement.scrollTop=10"
driver.execute_script(js2)
time.sleep(3)
#将页面滚动条拖到100个像素点
js3="var q=document.documentElement.scrollTop=100"
driver.execute_script(js3)
time.sleep(3)

driver.quit()


