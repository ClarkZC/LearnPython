# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:52:02 2019
逻辑错误的调试
@author: axt
"""


n=int(input("请输入n:"))
result=[]
factor=2
while factor*factor <= n:
    while (n%factor)==0:
        n //=factor
        result.append(factor)
        print(n,factor)
    factor+=1
if n>1:
    result.append(n)
print(result)