#coding=utf-8
import smtplib
# 导入 email 模块，MIMEText 和 Header 主要用来完成邮件内容与邮件标题的定义。
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTPException

#发送邮箱
sender="fzq003tdcq@126.com"
#接收邮箱
receiver="286330540@qq.com"
#发送邮箱主题
subject="明天我们去打球吧，打完球一起写作业"
#发送邮箱服务器
smtpserver="smtp.126.com"
#发送邮箱用户/密码
username='fzq003tdcq@126.com'
password='159753ai'

#中文需参数'utf-8'，单字节字符不需要
# msg = MIMEText('hello','plain','utf-8')
msg = MIMEText('北京时间，2017年11月19日，发送邮件失败，不知道是什么原因，这次不知道能不能成功','plain','utf-8')
msg['Subject'] = Header(subject,'utf-8')
# msg['From'] = sender
# msg['To'] = receiver
# try:
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
    # smtp = smtplib.SMTP(smtpserver,timeout=30)
smtp.login(username, password)
smtp.sendmail("fzq003tdcq@126.com", "286330540@qq.com", msg.as_string())
smtp.quit()
#     print "Success!"
# except smtplib.SMTPException,e:
#     print "Falied,%s"%e 


# 只赋值了msg['Subject'], 没有赋值msg['From'], msg['To']，导致出现554情况，更改了后就好了。
# 注意MIMEText初始化的时候，中文的第二个参数要用'plain'，我用'text',中文就显示不出来。
# msg['From'] 中人名为Tim，会和下面对应起来。




