#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 17:14
# @Author : ZY
# @File : Demo08_while循环嵌套应用.py
# @Project : code
"""
1,需求：打印星号（正方形）
*****
*****
*****
*****
*****
"""
a = 0
while a < 5:
    a += 1
    b = 0
    while b < 5:
        b += 1
        print('*', end='')
    print()

print("=" * 20)
"""
2，需求：打印星号(三角形)
*
**
***
****
*****
"""
a = 0
while a < 5:
    a += 1
    b = 0
    while b < a:
        b += 1
        print("*", end="")
    print()

print("=" * 20)
"""
3,需求：9*9乘法表
"""
a = 0
while a < 9:
    a += 1
    b = 0
    while b < a:
        b += 1
        print(f"{b}*{a}={a * b}\t", end='')
    print()
