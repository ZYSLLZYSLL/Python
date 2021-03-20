#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/23 9:10
# @Author : ZY
# @File : 判断字符串是否回文.py
# @Project : code
"""
    判断字符串是否回文
    全部字符串能对称
"""

values = input('请输入一串字符串：')

num = 0

if len(values) % 2 == 0:
    for i in range(len(values) // 2):
        if values[i] == values[-1 - i]:
            num += 1
else:
    for i in range(len(values) // 2):
        if i != (len(values) + 1) and values[i] == values[-1 - i]:
            num += 1

if num == len(values) // 2:
    print(f'{values} 是回文')
else:
    print(f'{values} 不是回文')
