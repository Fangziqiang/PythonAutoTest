#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import IGNORED_EXCEPTIONS

driver = webdriver.Firefox()
driver.get("http:www.baidu.com")

#WebDriverWait()方法使用
#    WebDriverWait(driver,timout,poll_frequency=0.5,ignored_exceptions=None)
#    driver-webdriver的驱动程序（Ie，Firefox,Chrome或远程）
#    timeout- 最长超时时间，默认以秒为单位
#    poll_frequency- 休眠时间的间隔（步长）时间，默认为0.5秒
#    ignored_exceptions-超时后的异常信息，默认情况下抛NoSuchElementException异常。

# WebDriverWait()一般由until或until_not()方法配合使用，下面是until和until_not方法的说明
#     until(method,message='')
#     调用该方法提供的驱动程序作为一个参数，直到返回值不为false
#     until_not(method, message=’’)
#     调用该方法提供的驱动程序作为一个参数，直到返回值为 False。
#     lambda
#     lambda 提供了一个运行时动态创建函数的方法。
#          1单个参数的：
#             g = lambda x:x*2
#             print g(3)
#             结果是6
#              
#          2多个参数的：
#             m = lambda x,y,z: (x-y)*z
#             print m(3,1,2)
#             结果是4
#          没事写程序的时候多用用python lambda就熟练了。。

element=WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_id("kw"))
element.send_keys("selenium")
# 判断id为kw元素是否消失
# is_disappeared = WebDriverWait(driver, 10, 1).\
#     until_not(lambda x: x.find_element_by_id("kw").is_displayed())
# print is_disappeared


#添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()

#添加固定休眠时间
time.sleep(5)


driver.quit()
