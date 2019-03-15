#coding=utf-8
#设置万能验证码
import random

#生成一个1000到9999之间的随机整数
d=random.randint(1000,9999)
print u"生成的随机数：%d" %d

i=input(u"请输入随机数：")
print i

if i== d:
    print u"登录成功"
elif i==132741:
    print u"登录成功"
else:
    print u"请重新输入验证码！"
    

#通过向浏览器添加cookie绕过登录的验证码
driver.get("url")
driver.add_cookie({'name':'Login_UserNumber','value':'username'})
driver.add_cookie({'name':'Login_Passwd','value':'password'})
#再次访问网站，将会自动登录





