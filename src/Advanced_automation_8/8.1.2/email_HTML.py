#coding=utf-8

# 参考网址
# http://www.runoob.com/python/python-email.html
import smtplib
# 导入 email 模块，MIMEText 和 Header 主要用来完成邮件内容与邮件标题的定义。
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱
sender="fzq003tdcq@163.com"
#接收邮箱
receiver="286330540@qq.com"
#发送邮箱主题
subject="python email test"
#发送邮箱服务器
smtpserver="smtp.163.com"
#发送邮箱用户/密码
username='fzq003tdcq@163.com'
password='159753ai'

#HTML形式的文件内容
msg=MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject']=subject
msg['From'] = sender
msg['To'] = receiver

smtp = smtplib.SMTP()
smtp.connect(smtpserver,25)
# smtp = smtplib.SMTP(smtpserver,timeout=30)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()


