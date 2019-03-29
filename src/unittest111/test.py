#coding=utf-8
import count

#import count 引入 count 文件，调用 add() 函数并传相应的值，通过获取的返回结果 f 与预期结果进行
#比较，如果不相等，将打印输出定义的 msg ，如果相等打印输出“test ok!” 
#整数相加
def test_add():
    try:
        f=count.add(2, 3)
        assert(f==4),'Integer addition result error!'
    #msg定义为'Integer addition result error!'
    except AssertionError,msg:
        print msg
    else:
        print 'test OK!'
#__name__和__main__都是两个下划线
if __name__=="__main__":
    test_add()