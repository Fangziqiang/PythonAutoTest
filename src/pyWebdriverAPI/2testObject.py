#coding=utf-8
1、clear():用于清除输入框的默认内容
2、send_keys("XX"):用于在一个输入框里输入XX内容
#python 是个容易出现编码问题的语言，有时候当我们在 send_keys()方法中输入中文时，然后脚本在
#运行时就报编码错误，这个时候我们可以在脚本开头声明编码为 utf-8，然后在中文字符的前面加个小u 就
#解决了（表示转成 python Unicode 编码）：send_keys(u"中文内容")
3、click():用于单击一个按钮
4、submit():提交表单
5、size:返回元素的尺寸。
size=driver.find_element_by_id("kw1").size
print size
6、text:获取元素的文本
#例：text=driver.find_element_by_id("kw1").text
   print text
7、get_attribute(name):获得属性值。
#返回元素的属性值，可以使id、name、type或元素拥有的其他任意属性
attribute=driver.find_element_by_id("kw1").getAttribute('type')
print attribute
8、is_displayed() 设置该元素是否用户可见。
#返回元素的结果是否可见，返回结果为True或False
result=driver.find_element_by_id("kw1").is_displayed()
print result







