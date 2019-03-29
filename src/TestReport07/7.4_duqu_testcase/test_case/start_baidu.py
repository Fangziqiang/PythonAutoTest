#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time,re,HTMLTestRunner
import unittest

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一个警告。
        self.accept_next_alert = True
    
    #百度搜索用例
    def test_baidu_search(self):
        #添加注释
#       三引号的注释会出现在测试报告中“test_baidu_search: 百度搜索测试”
        u'''百度搜索测试test'''
        driver =self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    
    #百度设置用例
    def test_baidu_set(self):
        u'''百度设置测试'''
        driver=self.driver
        driver.get(self.base_url+"/gaoji/preferences.html")
        
        #设置每页搜索结果为50条
        m = driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)
        
        #保存设置的信息
        driver.find_element_by_xpath("/html/body/form/div/input").click()
        time.sleep(2)
        driver.switch_to_alert().accept()
    
    #tearDown 方法在每个测试方法执行后调用，这个地方做所有测试用例执行完成的清理工作，如退出浏览器等。
# self.assertEqual([], self.verificationErrors)
# 这个是难点，对前面 verificationErrors 方法获得的列表进行比较；如查 verificationErrors 的列表
# 不为空，输出列表中的报错信息。
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
  
if __name__=="__main__":
    #unittest.main()函数用来测试类中以test开头的测试用例
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        