#coding=utf-8

# 运行测试集：
#     UnitTest 使用 TestRunner 类作为测试用例的基本执行环境，来驱动整个单元测试过程。Python 开发人
#     员在进行单元测试时一般不直接使用 TestRunner 类，而是使用其子类 TextTestRunner 来完成测试，并将测
#     试结果以文本方式显示出来：
#         runner = unittest.TextTestRunner()
#         runner.run(suite)
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

#测试
if __name__=="__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Mytest("test_add"))
    suite.addTest(Mytest("test_add2"))
    suite.addTest(Mytest("test_add3"))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

    
