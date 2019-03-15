#coding=utf-8
from time import sleep,ctime

def music(func):
    for i in range(2):
        print "I was listening to %s! %s" %(func,ctime())
        sleep(2)

def movie(func):
    for i in range(2):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)

if __name__=="__main__":
    music(u'爱情买卖')
    movie(u'阿凡达')
    print 'all end:',ctime()
