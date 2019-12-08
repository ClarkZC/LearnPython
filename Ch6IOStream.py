# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:14:21 2019

@author: axt
"""

import sys
total=0.0
count=0
for line in sys.stdin:
    count+=1
    total+=float(line)
avg=total/count
print("平均值为:",avg)