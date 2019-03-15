#coding = utf-8
filename = raw_input('please input file name:')
if filename == 'hello':
    raise NameError('input filename erro!')
#########################################################
####------异常------###-------描述------###                        
# AssertionError        assert语句失败
# AttributeError        试图访问一个对象没有的属性
# IOError               输入输出异常，基本是无法打开文件
# ImportError           无法引入模块或者包，基本是路径问题
# IndentationError      语法错误，代码没有正确的对齐
# IndexError            下标索引超出序列边界
# KeyError              试图访问你字典里不存在的键
# KeyboardInterrupt     Ctrl+C被按下
# NameError             使用一个还未赋予对象的变量
# SyntaxError           python代码逻辑语法出错，不能执行
# TypeError             传入的对象类型与要求不符
# UnboundLocalError     试图访问一个还未设置的全局变量，基本上是由于另有一个同名的全局变量，导致你以为在访问
# ValueError            传入一个不被期望的值，即使类型正确
#########################################################