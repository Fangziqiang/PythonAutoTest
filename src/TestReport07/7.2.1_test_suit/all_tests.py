#coding=utf-8
import unittest
#这里需要导入测试文件
import baidu,youdao

testunit=unittest.TestSuite()

#将测试用例加入到测试容器（套件）中
# makeSuite 用于生产 testsuite 对象的实例，把所有的测试用例组装成 TestSuite，最后把 TestSuite 传给
# TestRunner 进行执行。
# baidu 为导入的.py 文件，Baidu 为类名，调用类名，默认类下面的所有以 test 开头的方法（测试用例）会被执行。
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))

#执行测试套件
runner=unittest.TextTestRunner()
runner.run(testunit)