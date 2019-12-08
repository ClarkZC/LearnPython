# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:49:41 2019
循环结构
@author: axt
"""

#1 range
print("range==========")
for i in range(1,10):
    print(i,end=",")

print()
for i in range(10):
    print(i,end=",")
# for 
print()
print("for==========")
for i in (1,2,3):
    print(i,i*i)
    
print("100内所有3的倍数的和==========")
sum_3=0
for i in range(1,101):
    if i%3==0:
        sum_3+=i
print(sum_3)

# while
print("用公式求e的值==========")

i=1;e=1;t=1

while (1/t>=pow(10,-6)):
    t*=i
    e+=1/t
    i+=1
print("e=",e)

print("乘法九九表,下三角==========")
for i in range(1,10):
    s=""
    for j in range(1,i+1):
        s+=str.format("{0:1}*{1:1}={2:<2} ",i,j,i*j)
    print(s)
    
print("迭代法求平方根==========")
PSILON=1e-15                      #容差
a=float(input("请输入正实数a: "))
t=a
while(abs(t-a/t)>PSILON*t):
    t=(a/t+t)/2
print(t)

print("输出20项斐波那契数列==========")
f1=1;f2=1
for i in range(1,11):
    print(str.format("{0:6} {1:6}",f1,f2),end=" ")
    if i%2==0: print(" ")
    f1+=f2;
    f2+=f1;





