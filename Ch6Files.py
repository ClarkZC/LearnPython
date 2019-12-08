# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:46:21 2019

@author: axt
"""

fileName="fileTest.txt"                    #此为相对路径名，在程序文件所在目录现建立一个fileTest.txt文件，并输入几行内容
f=open(fileName,'r',encoding='GBK')  #    文件中包含中文，最好使用=’gbk',全英文的最好使用‘utf-8'
lineNo=0;
while True:
    lineNo+=1
    line=f.readline()
    if line:
        print(lineNo,":",line)
    else:
        break
f.close()

'''实现文件上下文操作的方法'''
lineNo=0
with open(fileName,'r',encoding='GBK') as f:
    for line in f:
        lineNo+=1
        print (lineNo,":",line)
        
