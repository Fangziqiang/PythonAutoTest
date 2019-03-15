#coding=utf-8
import smtplib
from email.mime.text import MIMEText
_user = "286330540@qq.com"
_pwd  = "njqyoxfpanqzbgfb"
_to   = "fzq003tdcq@163.com"

msg = MIMEText("Testsmtplib.SMTPDataError: (554, 'DT:SPM 163 smtp7,")
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e 