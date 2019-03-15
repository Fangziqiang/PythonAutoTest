#coding=utf-8
#普通函数
def fun(x):
    return x*2
print fun(5)

#匿名函数
# 用 lambda 来声明匿名函数，冒号（：）前面 x 表示参数，冒号后面 x*2 表示返回值。lambda 和普通
# 的函数相比，省去了函数名称，“匿名函数”也是由此而来。
f=lambda x:x*2
print f(5)