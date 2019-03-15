#coding=utf-8
lists=['c.txt','b.txt','d.txt','a.txt']

#取数组中的key做排序
def lists1():
    lists.sort(key=lambda lists:lists[1])
    print lists
    
def lists2():
    lists.sort(key=lambda lists:lists[0])
    print lists
# lists:lists[0] 表示取的是每个元组中的前半部分，即为：c、b、d、a ，所以可进行排序。
# lists:lists[1] 表示取的是每个元组中的后半部分，即为：txt ，不能有效的进行排序规律，所以按照数
# 组的原样输出。
lists1()
lists2()