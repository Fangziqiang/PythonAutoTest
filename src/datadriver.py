#coding=utf-8
#数据驱动的几种方式
#读取txt文件
from selenium import webdriver
import xlrd,time,HTMLTestRunner,unittest
from cus_fun import *
from time import sleep
from pydoc import source_synopsis
import os

# source = open("T_ic_csh.txt","r")
# users=source.readlines()
# source.close()
#执行循环
#for serch in users: 

def login(serch):
    driver=webdriver.Firefox()
    #driver=webdriver.Ie()
    driver.get("http://192.168.20.102:8080/mbcp/ssoLogin.jsp")
    #driver.maximize_window()
    driver.find_element_by_id('userName').clear()
    driver.find_element_by_id('userName').send_keys(serch)
    driver.find_element_by_id('userPass').clear()
    driver.find_element_by_id('userPass').send_keys("jadl123456")
    driver.get_screenshot_as_file('F:\\a.png')
    img_vcode = driver.find_element_by_id('validatecodeimg')
    location = img_vcode.location
    range = [int(location['x']),int(location['y']),int(location['x']+57),int(location['y']+40)]
    vcode = dis_vcode('F:\\a.png',range,'F:\\b.png')
    print vcode
    driver.find_element_by_id('vadidatecode').send_keys(vcode)
    #wait.until(lambda ele : ele.find_element_by_id('menu_030000')).click()
    #all_handles_0 = driver.window_handles
    driver.find_element_by_id('imageField').click()
    driver.close()
    
source = open("T_ic_csh.txt","r")
users=source.readlines()
source.close()
#执行循环
for serch in users: 
    serch=serch.strip('\n')
    login(serch)
#python 去掉字符串末尾换行符
#for line in file.readlines():
#   line=line.strip('\n')

        
    