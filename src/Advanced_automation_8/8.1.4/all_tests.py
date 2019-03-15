#coding=utf-8
import unittest

#把test_case目录添加到path下，这里用的是相对路径
import sys
sys.path.append("\test_case")
from test_case import baidu
from test_case import youdao
import smtplib
import os,time,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import HTMLTestRunner

#这里需要导入测试文件
# import baidu,youdao
# 三引号用于表示多行注释，同样三引号也不分单双，而且我们可以把一个多行注释做为一个字符串赋值给一个变量。

#==========定义发送邮件=============
# 定义一个 sentmail()发邮件函数，接收一个参数 file_new，表示接收最新生成的测试报告文件
def sentemail(file_new):
    #发信邮箱
    mail_from="286330540@qq.com"
    #收信邮箱
    mail_to="286330540@qq.com"
    _user = "286330540@qq.com"
    _pwd  = "njqyoxfpanqzbgfb"
    #定义正文
#     以读写（rb）方式打开最新生成的测试报告文件
    f=open(file_new,'rb')
#     读取文件内容，将内容传递给 mail_body。
    mail_body=f.read()
    f.close()
#     文件内容写入到邮件正文中。html 格式，编码为 utf-8。
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    print u'定义标题'
    msg['Subject']=u"百度测试报告"
    msg['From']=_user
    msg["To"]=mail_to
    #定义发送时间
    # msg['date']=time.strftime('%a,%d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP_SSL()
    print u'连接QQ邮件服务器'
    smtp.connect('smtp.qq.com',465)
    #用户名密码
    print u'使用用户名密码登录邮箱'
    smtp.login(_user, _pwd)
    print u'发送邮件'
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    print u'退出'
    smtp.quit()
    print 'email has send out!'

#==========查找测试报告目录，找到最新生成的测试报告文件=============
# 定义 sendreport()用于找最新生成的测试报告文件 file_new。调用并将 file_new 传给 sentmail()函数
def sendreport():
    result_dir="G:\\eclipse-workspace\\Advanced_automation_8\\codes\\8.1.4\\report"
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn) 
               if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生成的报告：'+lists[-1])
    #找到最新生成的文件
    file_new=os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    sentemail(file_new)
#+++++++++++测试用例组装测试套件++++++++++++
listaa="G:\\eclipse-workspace\\Advanced_automation_8\\codes\\8.1.4\\test_case\\"
def creatsuit():
    testunit=unittest.TestSuite()
    #discover方法定义
    discover=unittest.defaultTestLoader.discover(listaa,pattern='start_*.py',top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTests(test_case)
    print testunit
    return testunit

# 将测试用例加入到测试容器（套件）中
# makeSuite 用于生产 testsuite 对象的实例，把所有的测试用例组装成 TestSuite，最后把 TestSuite 传给TestRunner 进行执行。
# baidu 为导入的.py 文件，Baidu 为类名，调用类名，默认类下面的所有以 test 开头的方法（测试用例）会被执行。
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))

# 执行测试套件
# runner=unittest.TextTestRunner()
# runner.run(testunit)

#+++++++++++++定义并生成测试报告++++++++++++++++++++++
alltestnames=creatsuit()
# 获取当前时间
now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
#定义报告存放路径，支持相对路径
#把当前时间加到报告中
#filename = "D:\\selenium_python\\report\\"+now+'result.html'
filename = "report\\"+now+"result2.html"
fp=file(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')
runner.run(alltestnames)
# 遇到报告为空情况。
# 问题查找：发现是由于文件未关闭导致的
# 解决方法：加文件关闭语句f.close()便可以解决
fp.close()#关闭生成的报告
#执行发邮件
sendreport()