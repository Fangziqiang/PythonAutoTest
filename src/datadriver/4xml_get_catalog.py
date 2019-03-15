#coding=utf-8
#xml 有如下特征：
# 首先，它是有标签对组成：<aa></aa>
# 标签可以有属性： <aa id=’123’></aa>
# 标签对可以嵌入数据： <aa>abc</aa>
# 标签可以嵌入子标签（具有层级关系）：
# <aa>
# <bb></bb>
# </aa>
import xml.dom.minidom
#打开xml文档
dom=xml.dom.minidom.parse('abc.xml')
#得到文档元素对象
#documentElement 用于得到 dom 对象的文档元素，并把获得的对象给 root
# 每一个结点都有它的 nodeName，nodeValue，nodeType 属性
root = dom.documentElement
#1-获得标签信息-----------##################
print "------------------------------"
print u"1、打印标签信息："
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE

#2-获得标签的子标签--------##################
#对于知道标签名字的子标签，可以使用getElementByTagName方法获取：
mm=root.getElementsByTagName('maxid')
m=mm[0]
print "------------------------------"
print u"2、打印子标签信息:"
print m.nodeName

#3-区分相同标签名字的标签-------###############
#<caption>和<item>标签不止一个如何区分？
# root.getElementsByTagName('caption') 获得的是标签为 caption 一组标签；
#     b[0] 表示一组标签中的第一个；
#     b[2] 表示这一组标签中的第三个。
cc_tagname=root.getElementsByTagName('caption')
c=cc_tagname[2]
print "------------------------------"
print u"3、区分相同标签名字的标签:"
print c.nodeName

#4-获得标签对之间的数据--------------------#############
c1=cc_tagname[0]
print "------------------------------"
print u"4、获得标签对之间的数据:"
# firstChild 属性返回被选节点的第一个子节点，.data 表示获取该节点的数据。
print u"第一个caption标签对之间的数据为 :%s" %c1.firstChild.data

c2=cc_tagname[1]
print u"第二个caption标签对之间的数据为 :%s" %c2.firstChild.data

c3=cc_tagname[2]
print u"第三个caption标签对之间的数据为 :%s" %c3.firstChild.data


#5—1获得标签的属性所对应的值---getAttribute 方法可以获得元素的属性所对应的值。#####
ii_tagname=root.getElementsByTagName('item')
i=ii_tagname[1]
i1=ii_tagname[0]
print "------------------------------"
print u"item的nodeName为:%s" %(i.nodeName)
print u"5、获得标签的属性所对应的值:"
id1=i1.getAttribute("id")
print id1

i2=ii_tagname[1]
id2=i2.getAttribute("id")
print id2

#6-2获得标签的属性所对应的值------------#################
ll_list=root.getElementsByTagName('login')
l=ll_list[0]

un=l.getAttribute("username")
print un
pd=l.getAttribute("passwd")
print pd

print l.nodeName










