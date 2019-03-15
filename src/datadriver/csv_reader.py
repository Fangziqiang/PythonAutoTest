#coding=utf-8

from selenium import webdriver
import csv
import codecs

file_path = 'G:\\Program Files\\eclipse\\workspace\\1111\\src\\datadriver\\csv_test.csv'
# userinfo=csv.reader(file(file_path,'rb'))
# userinfo2=userinfo.decode('GB2312').encode('utf-8')
u=codecs.open(file_path,'r','utf-8')
userinfo=u.readlines()
u.close()

for info in userinfo:
    print info

