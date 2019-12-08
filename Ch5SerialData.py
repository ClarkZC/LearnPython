# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:58:51 2019
系列数据类型
@author: axt
"""

t1=(1,2,3,4,5)  #元组
t2=('a',12,12,False,"Hello")
lst1=[1,2,3,4,5,6]
str1="MyHeart"
print(t1[1],t2[3],str1[2])  #读取元素

print(len(t1))           #len() 返回长度
print(len(t2))
print(len(lst1))
print(len(str1))

print("切片操作**************")
print(t1[0:3])  #不包含结束位置
print(t2[:4:2])
print(lst1[-3:-1])

print('连接与重复**************')
print(t1+t2)
print(t1*2)

print('成员操作**************')
x=12
print(x in t2)
print(t2.count(x))
print(t2.index(x))

print("系列拆封**************")
a,b=(12,23)
print(a)
print(b)
data=(1001,"张三",(80,79,92))
sid,name,score=data
print(score)
sid,name,(Chinese,Mathes,English)=data
print(Mathes)

first,*middle,last=sorted([70,85,89,88,86,95,89]) # 去掉最高和最低分求平均分
print("平均分为：",sum(middle)/len(middle))


_,e,_=(1,2,3)   #临时变量_
print(e)

l1=['a',5,6]
l1[:2]='b'
print(l1) 

print("列表解析**********")
print([i**2 for i in range(10)])
print([(i,i**2) for i in range(6)])
print([i for i in range(10) if i%2==0])  #输出偶数
print([(x,y,x*y) for x in range(1,4) for y in range(1,4) if x>=y])

print(b"abc\'")



