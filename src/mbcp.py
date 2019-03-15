#coding=utf-8
from selenium import webdriver
import xlrd,time,HTMLTestRunner,unittest
from cus_fun import *
from time import sleep
def login():
    driver=webdriver.Firefox()
#     driver=webdriver.Ie()
    driver.get("http://192.168.20.102:8080/mbcp/ssoLogin.jsp")
    #driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_id('userName').send_keys('myx')
    driver.find_element_by_id('userPass').send_keys('jadl123456')
    time.sleep(1)
    #driver.find_element_by_class_name('code').send_keys('6728')
    #ʶ����֤��:������֤������ҳ���ͼ
    driver.get_screenshot_as_file('F:\\a.png')
    #ʶ����֤��:��ȡ��֤��ͼƬ������,������֤���ȡ�ķ�Χ
    img_vcode = driver.find_element_by_id('validatecodeimg')
    location = img_vcode.location
    range = [int(location['x']),int(location['y']),int(location['x']+57),int(location['y']+40)]
    #ʶ����֤��:�����Զ��庯����ʶ��������֤��
    vcode = dis_vcode('F:\\a.png',range,'F:\\b.png')
    print vcode
    #driver.find_element_by_id('vadidatecode').send_keys(vcode)
    time.sleep(1)
    driver.find_element_by_id('vadidatecode').send_keys(vcode)
    #driver.find_element_by_id('imageField').click()
    #wait.until(lambda ele : ele.find_element_by_id('menu_030000')).click()
    all_handles_0 = driver.window_handles
    driver.find_element_by_id('imageField').click()
    
login()
    


        
    