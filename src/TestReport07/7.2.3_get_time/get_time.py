#coding=utf-8
import time

print time.time()         #获取当前时间戳
print time.localtime()    #当前时间的struct_time形式
print time.ctime()        #当前时间的字符串形式
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())