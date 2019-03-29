#coding=utf-8
import sys
sys.path.append("\test_case")
from test_case import start_youdao
from test_case import start_baidu

#用例文件列表
def case_list():
    alltestnames =[
        start_baidu.Baidu,
        start_youdao.Youdao,
        # webcloud.Login,
        ]
    print "success read case list!!"
    
    return alltestnames