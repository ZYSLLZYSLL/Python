#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 16:01
# @Author : ZY
# @File : Demo02_if_分段函数.py
# @Project : code

"""
有一个分段函数，当x<1,1<=x<10,x>=10时分别对应y=x,y=2x-1,y=3x+6,输入任意x,求y
"""
x = int(input("请输入X的值："))

if x < 1:
    y = x
elif 1 <= x < 10:
    y = 2 * x - 1
else:
    y = 3 * x + 6
print(f"当X={x}时Y={y}")
