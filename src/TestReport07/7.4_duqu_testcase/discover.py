#coding=utf-8
import unittest
import HTMLTestRunner
import os,time

################dicover解决用例的读取##########################################
#  unittest 的 TestLoader 成员下面提供了discover()方法，可以通过文件的名称来判断是否为测试用例文件，
# 如果为用例文件则自动添加到测试套件中
#     TestLoader:测试用例加载器，其包括多个加载测试用例的方法。返回一个测试套件
#     discover(start_dir，pattern='test*.py'，top_level_dir=None)
#         找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名才能被加载。
# 如果启动的不是顶层目录，那么顶层目录必须要单独指定。   
#         start_dir  ：要测试的模块名或测试用例目录。
#         pattern='test*.py'：表示用例文件名的匹配原则。星号“*”表示任意多个字符。
#    top_level_dir=None：测试模块的顶层目录。如果没顶层目录（也就是说测试用例不是放在多级目录
# 中），默认为 None。

listaa="G:\\eclipse-workspace\\Test_report_7\\src\\07\\7.4_duqu_testcase\\test_case\\"
def creatsuite1():
    testunit=unittest.TestSuite()
    #discover方法定义
    discover=unittest.defaultTestLoader.discover(listaa,
                      pattern='start_*.py',
                      top_level_dir=None)
#     print discover
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    print testunit
    return testunit
alltestnames = creatsuite1()

# 获取当前时间
now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
# 定义报告存放路径，支持相对路径
# 把当前时间加到报告中
#filename = "D:\\selenium_python\\report\\"+now+'result.html'
filename = "report\\"+now+"result2.html"
fp=file(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况')
#执行测试用例
runner.run(alltestnames)
    
    
    
    