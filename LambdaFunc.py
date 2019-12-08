# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:56:00 2019
Lambda表达式和匿名函数
@author: axt
"""
f=lambda x,y:x+y
print(type(f))

print(f(12,13))

for i in filter(lambda x:x>0,[1,0,-2,8,15]):
    print(i)
