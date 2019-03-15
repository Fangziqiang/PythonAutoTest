#coding=utf-8

import time
try:
    f=file('poem.txt')
    while True:# our usual file-reading idiom
        line=f.readline()
        if len(line)==0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up...closed the file'
#1
print '#1'
try:
    open("abc.txt",'r')
except IOError:
    pass
#2
print '#2'

try:
    print aa
#这里应该使用NameError
except IOError:
    pass
#3
print '#3'
try:
    print aa
except NameError, msg:
    print msg