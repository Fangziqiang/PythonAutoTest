#coding=utf-8

#获取最新测试报告
import os,datetime,time
result_dir="G:\\Program Files\\eclipse\\workspace\\Test_report_7\\src\\07\\7.2.2_HTMLTestRunner\\report"

# os.listdir():用于获取目录下的所有文件列表
lists=os.listdir(result_dir)
print lists

#lists.sort()
# 1、Python 列表有一个内置的列表。sort()方法用于改变列表中元素的位置。还有一个 sorted()内置函数，
# 建立了一种新的迭代排序列表。
# 2、key 是带一个参数的函数，用来为每个元素提取比较值. 默认为 None, 即直接比较每个元素
# 3、lambda 提供了一个运行时动态创建函数的方法。我这里创建了 fn 函数。
# 4、os.path.getmtime()：getmtime()返回文件列表中最新文件的时间（最新文件的时间最大，所以我们会得到一个最大时间）
lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))

# -1表示取文件列表中的最大值，也就是最新被创建的值
print('最新的文件为:'+lists[-1])
# os.path.join()：join()方法用来连接字符串，通过路径与文件名的拼接，我们将得到目录下最新被创建的的文件名的完整路径。
file=os.path.join(result_dir,lists[-1])
print file