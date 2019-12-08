# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:57:16 2019
字符串基本语法和函数
@author: axt
"""

s='abcd"12"3'      #单引号包含的字符串可以有双引号
s1="abcd'234'"      #双引号包含的字符串可以有单引号
s3="""hello there!
It's a beautiful day,
isn't it?"""             #三个单引号或双引号包含的字符串可以换行

print(s.upper())   #字符串对象方法
print(str.upper(s3))

print(str(123.34) + '是实数')     #字符串转换方法str(),  字符串+ 连接运算要求两边都为字符串

'''字符串的格式化'''
print()
print(str.format("学生人数{0},平均成绩{1:2.2f}",15,81.2))
print('学生人数{0},平均成绩{1:2.2f}'.format(15,81.2))

print('1'.center(20))
print(format("121","^20"))
print(format("12321","^20"))
print("1".rjust(20,'*'))
print(format("121",'*>20'))
print(format("12321",'*<20'))

print(3**2**3)
