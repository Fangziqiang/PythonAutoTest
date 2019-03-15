#coding=utf-8

'''还记得上面提到的__init__.py 文件吧，这文件是干嘛的，为什么要在引用的目录下加这个文件？:
        要弄明白这个问题，首先要知道，python 在执行 import 语句时，到底进行了什么操作，按照 python 的文
档，它执行了如下操作：
第 1 步，创建一个新的，空的 module 对象（它可能包含多个 module）；
第 2 步，把这个 module 对象插入 sys.module 中
第 3 步，装载 module 的代码（如果需要，首先必须编译）
第 4 步，执行新的 module 中对应的代码。
在执行第 3 步时，首先要找到 module 程序所在的位置，搜索的顺序是：
当前路径 （以及从当前目录指定的 sys.path），然后是 PYTHONPATH，然后是 python 的安装设置相关的
默认路径。正因为存在这样的顺序，如果当前路径或 PYTHONPATH 中存在与标准 module 同样的 module，则
会覆盖标准 module。也就是说，如果当前目录下存在 xml.py，那么执行 import xml 时，导入的是当前目录下
的 module，而不是系统标准的 xml。
了解了这些，我们就可以先构建一个 package，以普通 module 的方式导入，就可以直接访问此 package
中的各个 module 了。python 中的 package 必须包含一个__init__.py 的文件。'''
# 理解了上面这段话也就明白了为什么，all_tests.py 和测试用例（.py）文件在一个目录下时可以正
# 常调用，移出来之后就提示找不到模块了；
# python 查找模块是先从当前目录下查找，如果找不到再到python 的安装设置的相关路径下查找。
# 这也是为什么我们把 D:\selenium_python\test_cast 目录添加到
# 系统 path 下，就可以正常的调用了。为了标识一下目录是可引用的包，那么就需要在目录下创建一个__init__.py 文件。


