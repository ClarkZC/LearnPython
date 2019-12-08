# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:15:55 2019
函数
@author: axt
"""
def print_star(n):
    print(("*"*n).center(50))

#n=int(input("请输入要打印的行数？"))
m=10
for i in range(1,2*m,2):
    print_star(i)

'''计算分数数列和1/2+1/3+1/4.。。1/n'''
def harmonic(n):
    total=0.0
    for i in range(2,n):
        total+=1.0/i
    return total

print(harmonic(m))