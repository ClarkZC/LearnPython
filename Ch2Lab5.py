# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:22:52 2019

@author: axt
"""
import datetime

name=input("请输入您的姓名:")
birth_year=int(input("请输入您的出生年份:"))

age=datetime.date.today().year - birth_year  #系统当前年份减去出生年份

print("{0}您好，您今年{1}岁.".format(name,age))
