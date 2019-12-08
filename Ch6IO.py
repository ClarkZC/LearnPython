# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:00:31 2019

@author: axt
"""

"""input and print**************"""
print(1,2,3)
print(1,2,3, sep=',')
print(1,2,3, sep=',', end='.\n')
for i in range(5):
    print(i,end=' ')       #非独占一行，而是以空格间隔
   
import datetime
sName=input("请输入姓名：")
birthYear=int(input("请输入出生年份:"))
age=datetime.date.today().year-birthYear
print("{0}您好，您今年{1}岁".format(sName,age))


"""读取n个数，并求和"""

n=5
sumAll=0
for i in range(n):
    num=int(input("请输入整数："))
    sumAll += num
print('累加结果为：',sumAll)


'''交互式用户输入'''
a=[]     #初始化列表
x=float(input("请输入一个实数，输入-1终止："))
while x!=-1:
    a.append(x)
    x=float(input("请输入一个实数，输入-1终止："))
print("计数：",len(a))
print("求和：",sum(a))
print("平均值:",sum(a)/len(a))

'''运行时提示输入密码'''
import getpass
username=input("用户名：")
passwd=getpass.getpass("密码：")
if username=='clark' and passwd=='123456':
    print("登录成功")
else:
    print("登录失败")

