#coding=utf-8
import csv

# wb中的w表示写入模式，b是文件模式
# 写入一行用writerow
# 多行用writerows

csvfile=file('csv_test.csv','wb')
writer=csv.writer(csvfile)
writer.writerow(['姓名','年龄','电话'])
data = [
        ('小何','25','1234567'),
        ('小芳','18','789456')]
writer.writerows(data)

csvfile.close()