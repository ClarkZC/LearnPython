# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 08:32:04 2019
默认的输入流来自键盘，默认的输出流则为屏幕
@author: axt
"""

import sys
n=int(input("请输入n:"))
power=1
i=0
f=open('out.log','w')            #指定标准输出重定向到文件out.log中
sys.stdout=f                    #输出重定向到文件
while i<=n:
    print(str(i),' ',str(power))
    power*=2
    i+=1
sys.stdout=sys.__stdout__       #回复系统默认值
print('Done!')