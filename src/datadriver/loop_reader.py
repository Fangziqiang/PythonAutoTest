#coding=utf-8
import csv
import userinfo

#获取字典数据
info=userinfo.zidian()
#读取本地csv文件
my_file='G:\\eclipse-workspace\\1111\\src\\datadriver\\userinfo.csv'
datainfo=csv.reader(file(my_file,'rb'))
for us,pw in info.items():
    print us
    print pw
for user in datainfo:
    print user[0]
    print user[1]
    print user[2]
    print user[3]