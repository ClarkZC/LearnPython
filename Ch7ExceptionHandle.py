# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 22:21:28 2019
异常处理
@author: axt
"""

try:
    f=open("testfile.txt","w")
    f.write("这是测试异常处理代码的文件！")
    f1=open("testfile1.txt","r")  
except IOError:
    print("没有找到文件或读取失败")
else:
    print("文件写入成功")
finally:
    f.close()