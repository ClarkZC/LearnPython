# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:24:33 2019

@author: axt
"""

a=1+2j
b=complex(4,5)       #复数4+5j
print(a+b)         #输出5+7j
print(a.real,a.imag)     #分别输出实部和虚部

import cmath      #引入复数数学库
print(cmath.sqrt(b))         #复数的平方根



