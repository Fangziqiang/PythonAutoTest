#coding=utf-8
# ActionChains类鼠标操作的常用方法：
# 1、context_click() 右击
# 2、double_click()  双击
# 3、drag_and_drop(source,target) 拖动
#source:鼠标按下的源元素
#target:鼠标释放的目标元素
# 4、move_to_element()  鼠标悬停在一个元素上
# 5、click_and_hold()   按下鼠标左键在一个元素上
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Ie()
#1、鼠标右击
#定位到要右击的元素
right=driver.find_element_by_xpath("xx")
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right).perform()
#2、鼠标双击
#定位到要双击的元素
double=driver.find_element_by_xpath("xxx")
#对定位到的元素执行双击操作
ActionChains(driver).double_click(double).perform()

#3、鼠标拖放操作
#定位元素的原位置
element=driver.find_element_by_name("xxx")
#定位元素要移动到的目标位置
target=driver.find_element_by_name("xxx2")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()

#4、鼠标移动到元素上
#定位到鼠标移动到上面的元素
above=driver.find_element_by_xpath("xxx3")
#对定位到的元素执行鼠标移动都上面的操作
ActionChains(driver).move_to_element(above).perform()

#5、按下鼠标左键
#定位到鼠标按下左键的元素
left=driver.find_element_by_xpath("xxx4")
#对定位到的元素执行鼠标左键按下的操作
ActionChains(driver).click_and_hold(left).perform()














