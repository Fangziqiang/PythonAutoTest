#coding=utf-8
from selenium import webdriver
import xlrd,time,HTMLTestRunner,unittest
from cus_fun import *
from time import sleep
def login():
    driver=webdriver.Firefox()
    driver.get("http://192.168.20.58:9999/mbxtwlfwpt/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_class_name('mima').send_keys('123456')
    #driver.find_element_by_class_name('code').send_keys('6728')
    #识别验证码:保存验证码所在页面截图
    driver.get_screenshot_as_file('F:\\a.png')
    #识别验证码:获取验证码图片的坐标,设置验证码截取的范围
    img_vcode = driver.find_element_by_id('validatecodeimg')
    location = img_vcode.location
    range = [int(location['x']),int(location['y']),int(location['x']+57),int(location['y']+40)]
    #识别验证码:调用自定义函数，识别并填入验证码
    vcode = dis_vcode('F:\\a.png',range,'F:\\b.png')
    print (vcode)
    #driver.find_element_by_id('vadidatecode').send_keys(vcode)
    driver.find_element_by_class_name('code').send_keys(vcode)
    #driver.find_element_by_id('imageField').click()
    #wait.until(lambda ele : ele.find_element_by_id('menu_030000')).click()
    all_handles_0 = driver.window_handles
    driver.find_element_by_class_name('login_btn').click()
    
login()
    

# class login:
#     def add(self,a,b):
#         c=a+b
#         print c
#     
#     def substract(self,a,b):
#         c=a-b
#         print c
#     def login(self):
#         self.driver=webdriver.Ie()
#         self.driver.get("http://192.168.20.58:9999/mbxtwlfwpt/")
        
        
    