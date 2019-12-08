# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:48:24 2019

@author: axt
"""

#Python分支结构

import datetime
score=int(input("输入分数:"))
if(score>=60):
    print("通过", end=":")
else:
    print("未通过",end=":")
    
if(score>=90):
     print("优秀")
elif(score>=80):         
     print("良好")
elif(score>=70):         
     print("中等")
elif(score>=60):         
     print("及格")
else:
    print("不及格")
    
y=datetime.date.today().year
if((y%4==0 and y%100!=0) or y%400==0):
    print("今年是闰年")
else:
    print("今年不是闰年")