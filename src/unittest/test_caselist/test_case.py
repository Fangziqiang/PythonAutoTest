#coding=utf-8
import os
#列出某个文件夹下所有case，这里用的是python所在.py文件运行一次后生成一个pyc的副本
# 相对路径
caselist = os.listdir('test_case')
# 绝对路径：
# caselist = os.listdir(u"G:\\eclipse-workspace\\UnitTest\\src\\test_caselist\\test_case")
for a in caselist:
    s = a.split('.')[1] #选取后缀名为py的文件
    if s=='py':
        #此处执行dos命令并将结果保存到log.txt
        # 相对路径
        # >>log.txt：将执行结果保存在当前目录下log.txt文件中
        os.system('test_case\\%s >>log.txt 2>&1'%a)
        # 绝对路径：
        # os.system(u"G:\\eclipse-workspace\\UnitTest\\src\\test_caselist\\test_case\\%s >>log.txt 2>&1"%a)
