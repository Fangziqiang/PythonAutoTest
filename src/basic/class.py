#coding=utf-8
#定义类：
#类的方法与函数有一个明显的区别，在类的方法中必须有个额外的第一个参数（self），但在调用类
#的方法时却不必为这个参数赋值。self 参数所指的是对象本身，所以习惯性地命名为 self。
class Counter:
    def add(self,a,b):
        c=a+b
        print (c)
    def subtract(self,a,b):
        c=a-b
        print (c)

# 创建实例
test = Counter()

test.add(1,2)
test.subtract(1,2)
