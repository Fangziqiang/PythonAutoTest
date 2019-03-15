#coding=utf-8
import os

# os.path.getmtime()
# getmtime()返回 文件列表中最新文件的时间（最新文件的时间最大，所以我们会得到一个最大时间）
# 如果判断的目录下面还包含有目录文件，我们需要进行更复杂的判断：
lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn)
           if not os.path.isdir(result_dir+"\\"+fn) else 0)
# if not .. 的用法刚好与 fi 相反， 表示：“如果条件不为真，将执行 if 后面的语句。”
# os.path.isdir():isdir()函数判断某一路径是否为目录。