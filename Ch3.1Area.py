# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:41:02 2019

@author: axt
"""

import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

h=(a+b+c)/2
area=math.sqrt(h*(h-a)*(h-b)*(h-c))
print(str.format("此三角形面积为：{0}",area))