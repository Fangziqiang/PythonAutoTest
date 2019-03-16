#coding=utf-8
import unittest,time,os,multiprocessing
import HTMLTestRunner

#查找含有thread的文件、文件夹
def EEEcreatsuit():
    casedir=[]
    listaa=os.listdir('D:\\flask\\test')
    for xx in listaa:
        if "thread" in xx:
            casedir.append(xx)
    
    suit=[]
    for n in casedir:
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(n,
                                                     pattern='*_sta.py',
                                                     top_level_dir=n)
    print discover
    for test_suit in discover:
        for test_case in test_suit:
            test
    
    
    
    