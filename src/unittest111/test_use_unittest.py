#coding=utf-8
import count

import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        self.js=count
    #整数相加
    def test_add(self):
        self.assertEqual(self.js.add(2, 3), 5)
    #小数相加
    def test_add2(self):
        self.assertEqual(self.js.add(2.3, 3.2), 5.5)
    #字符串相加
    def test_add3(self):
        self.assertEqual(self.js.add('hello', 'world'), 'hello world')
    
    def tearDown(self):
        pass

#构造测试集
# 提供名为 suite()的全局方法，UnitTest 在执行测试的过程调用 suit()方法来确定有多少个测试
# 用例需要被执行，可以将 TestSuite 看成是包含所有测试用例的一个容器。
def suite():
    suite = unittest.TestSuite()
    suite.addTest(Mytest("test_add"))
    
    return suite 
# Unittest从用例的编写上更加规范简洁，我们只用关注传参与预期结果，不需要手动添加打印信息。从用例的
# 执行结果来看，给出用例的执行个数，执行耗时等。如果用例执行失败则给出详细的错误信息，帮助我们
# 更好的定位错误原因。
if __name__=="__main__":
    unittest.main(defaultTest = 'suite')
    
