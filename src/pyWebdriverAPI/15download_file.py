#coding=utf-8
import requests
from selenium import webdriver
import os
#HTTP Content-type(内容类型)常用对照表: http://tool.oschina.net/commons
#Content-Type，内容类型，一般是指网页中存在的Content-Type,用于定义网络文件的类型和网页的编码
#决定浏览器将以什么形式、什么编码读取这个文件。要想下载文件，首先要确定你下载的文件的类型。

print requests.head('https://www.python.org').headers['content-type']
fp=webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
#指定你所下载文件的目录
#os.getcwd() 返回当前的目录
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.nerverAsk.saveToDisk",
                  "application/octet-stream")#下载文件的类型
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()