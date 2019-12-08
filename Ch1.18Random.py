# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:52:55 2019

@author: axt
"""

import random as rd
print("您今天的幸运数字是：",rd.choice(range(10)))
a=123
print(type(a))
print(id(a))
b=a
print(id(a))
#b=345
print(a)
print(b)
print(a==b)
print(a is b)
del a
#print(id(a))