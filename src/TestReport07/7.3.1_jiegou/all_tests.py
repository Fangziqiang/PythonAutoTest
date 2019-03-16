#coding=utf-8
import unittest

#把test_case目录添加到path下，这里用的是相对路径
import sys
sys.path.append("\test_case")
from test_case import baidu
from test_case import youdao

#这里需要导入测试文件
# import baidu,youdao
import HTMLTestRunner
import time
'''三引号用于表示多行注释，同样三引号也不分单双，而且我们可以把一个多行注释做为一个字符串赋
值给一个变量。'''

testunit=unittest.TestSuite()

#将测试用例加入到测试容器（套件）中
''' makeSuite 用于生产 testsuite 对象的实例，把所有的测试用例组装成 TestSuite，最后把 TestSuite 传给
 TestRunner 进行执行。
 baidu 为导入的.py 文件，Baidu 为类名，调用类名，默认类下面的所有以 test 开头的方法（测试用例）会被执行。'''
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))

# 执行测试套件
# runner=unittest.TextTestRunner()
# runner.run(testunit)

# 获取当前时间
now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
#定义报告存放路径，支持相对路径
#把当前时间加到报告中
#filename = "D:\\selenium_python\\report\\"+now+'result.html'
filename = "report\\"+now+"result2.html"
fp=file(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)
fp.close()


