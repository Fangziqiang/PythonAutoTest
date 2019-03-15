#coding=utf-8

# 我们应该避免使用 thread 模块，原因是它不支持守护线程。当主线程退出时，所有的子线程不论它
# 们是否还在工作，都会被强行退出。有时我们并不期望这种行为，这时就引入了守护线程的概念。threading
# 模块则支持守护线程。所以，我们直接使用 threading 来改进上面的例子。
# 引入线程模块
import threading
from time import time,ctime, sleep

def music(func):
    for i in range(2):
        print "I was listening to %s! %s"%(func,ctime())
        sleep(2)
def movie(func):
    for i in range(2):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)
# 创建用于装载线程的数组
threads=[]
# 创建线程
t1=threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)

t2=threading.Thread(target=movie,args=(u'阿凡达',))
threads.append(t2)

if __name__=="__main__":
    for i in threads:
#       start():开始线程活动
        i.start()
        
    print 'all end:%s'%ctime()






