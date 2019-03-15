#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱
sender="286330540@qq.com"
#接收邮箱
receiver="fzq003tdcq@163.com"
#发送邮箱主题
subject="python email test"
#发送邮箱服务器
smtpserver="smtp.qq.com"
#发送邮箱用户/密码
username='286330540@qq.com'
password='tztcbxrfedsocaha'

#中文需参数'utf-8'，单字节字符不需要
# msg = MIMEText('hellow','plain','utf-8')
msg = MIMEText('hellow','plain','utf-8')
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = sender
msg['To'] = receiver
try:
    # smtp = smtplib.SMTP()
    smtp =smtplib.SMTP_SSL("smtp.qq.com", 465)
    # smtp.connect(smtpserver,25)
    # smtp = smtplib.SMTP(smtpserver,timeout=30)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error:无法发送邮件"
# smtp.quit()


# 只赋值了msg['Subject'], 没有赋值msg['From'], msg['To']，导致出现554情况，更改了后就好了。
# 注意MIMEText初始化的时候，中文的第二个参数要用'plain'，我用'text',中文就显示不出来。
# msg['From'] 中人名为Tim，会和下面对应起来。




