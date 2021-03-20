#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 19:23
# @Author : ZY
# @File : Demo06_判断三角形.py
# @Project : code

# 需求：根据边判断三角形，直角，锐角，钝角
# a = int(input('请输入三角形的第一条边:'))
# b = int(input('请输入三角形的第二条边:'))
# c = int(input('请输入三角形的第三条边:'))
#
# if c < a:
#     a,c = c,a
# if c < b:
#     a,b = b,a
# if b < a:
#     a,b = b,a
#
# if a + b <= c:
#     print('啥都不是')
# else:
#     if (a ** 2 + b ** 2) == (c ** 2):
#         print('直角三角形')
#     elif (a ** 2 + b ** 2) < (c ** 2):
#         print('钝角三角形')
#     else:
#         print('锐角三角形')

z = input("请输入三角形三边长，数据用逗号','(英文)隔开:")
z = z.split(',')

a = int(z[0])
b = int(z[1])
c = int(z[2])

if c < a:
    a, c = c, a
if c < b:
    a, b = b, a
if b < a:
    a, b = b, a

if a + b <= c:
    print('啥都不是')
else:
    if (a ** 2 + b ** 2) == (c ** 2):
        print('直角三角形')
    elif (a ** 2 + b ** 2) < (c ** 2):
        print('钝角三角形')
    else:
        print('锐角三角形')
