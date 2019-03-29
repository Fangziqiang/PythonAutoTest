#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re 
import HTMLTestRunner

#Baidu类继承 unittest.TestCase 类，从 TestCase 类继承是告诉 unittest 模块的方式，这是一个测试案例。
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com/"
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一个警告。
        self.accept_next_alert = True
    #百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    #百度设置用例
    def test_baidu_set(self):
        driver = self.driver
        
        #进入搜索设置页
        driver.get(self.base_url+"/gaoji/preferences.html")
        #设置每页搜索结果为100条
        m=driver.find_element_by_name("NR")
        #定位下拉框
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)
        
        #保存设置的信息
        driver.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__=="__main__":
    unittest.main()
    