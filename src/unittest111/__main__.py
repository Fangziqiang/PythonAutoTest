#coding=utf-8

# UnitTest 模块中定义了一个名为 main 的全局方法，使用它可以很方便地将一个单元测试模块变成
# 可以直接运行的测试脚本，main()方法使用 TestLoader 类来搜索所有包含在该模块中的测试方法，并
# 自动执行它们。如果 Python 程序员能够按照约定（以 test 开头）来命名所有的测试方法，那就只需要
# 在测试模块的最后加入如下几行代码即可：
import count
import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        self.js=count
    #整数相加
    def test_add(self):
        self.assertEqual(self.js.add(2, 3), 5)
    #小数相加
    def test_add2(self):
        self.assertEqual(self.js.add(2.3, 3.2), 5.5)
    #字符串相加
    def test_add3(self):
        self.assertEqual(self.js.add('hello', ' world'), 'hello world')
    
    def tearDown(self):
        pass

#测试
if __name__=="__main__":
    unittest.main() 
#     # 构造测试集
#     suite = unittest.TestSuite()
#     suite.addTest(Mytest("test_add"))
#     suite.addTest(Mytest("test_add2"))
#     suite.addTest(Mytest("test_add3"))

    

    
