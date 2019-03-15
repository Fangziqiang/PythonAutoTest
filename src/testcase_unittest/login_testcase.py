#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import unittest
# Assert 失败时，该测试将终止。
# Verify 失败时，该测试将继续执行，并将错误记入日显示屏 。也就是说允许此单个 验证通过。确保应用程序在正确的页面上。
# Waitfor 用于等待某些条件变为真。可用于 AJAX 应用程序的测试。

#使用unittest
class Test(unittest.TestCase):
    def test_case(self):
        try:
            #driver = webdriver.Firefox()
            driver = webdriver.Ie()
            driver.get("https://pan.baidu.com/")
            
            driver.maximize_window()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='login-middle']/div/div[6]/div[2]/a").click()
            time.sleep(3)
            driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
            driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(u"听风AIF")
            driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("159753ai")
            driver.find_element_by_id("TANGRAM__PSP_4__memberPass").click()
            driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
            time.sleep(3)
            now_user=driver.find_element_by_class_name("user-name").text
            print now_user
            #使用unittest框架时不使用下面这句代码
            #assert(u"听风AIF"==now_user)   #失败时，该测试将终止。不失败才会执行下面的print
            self.assertEqual(now_user, "听风AI", msg=("the user is not 听风AI,is %s" %now_user))
            #self.assertEqual(u"听风AI",now_user)
            #print "现在登录用户是“听风AIF”"
            #assertEqual(now_user,"听风AIF"，msg="0k")
        except AssertionError,msg:
            print msg
            driver.quit()
if __name__=="__main__":
    unittest.main()
