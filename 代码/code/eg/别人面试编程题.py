#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/8 11:32
# @Author : ZY
# @File : 别人面试编程题.py
# @Project : code

"""
    1、有一分数序列:1/2,1/4,1/6, 1/8……，写一个函数，求此数列前20项的和。
    2、用户输入4位整数作为年份,判断其是否为闰年。(闰年判断条件，数字能被400整除，或者能被4整除但不能被100整除）
    3、生成包含15个随机数的列表，然后前10个降序排列，后5个升序排列，并输出结果。
    4、s="hello world",去重并进行升序排序输出
"""

# 1、有一分数序列:1/2,1/4,1/6, 1/8……，写一个函数，求此数列前20项的和。

# def sum_fenshu():
#     i = 2
#     a = 0
#     for j in range(20):
#         a += (1 / i)
#         i += 2
#
#
# sum_fenshu()

# 2、用户输入4位整数作为年份,判断其是否为闰年。(闰年判断条件，数字能被400整除，或者能被4整除但不能被100整除）

# def runNian():
#     i = int(input('请输入4位整数作为年份：'))
#     if i < 1000 or i > 9999:
#         print('请输入四位整数作为年份')
#     elif (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
#         print(f'{i}年是闰年')
#     else:
#         print(f'{i}年不是闰年')
#
#
# runNian()

# 3、生成包含15个随机数的列表，然后前10个降序排列，后5个升序排列，并输出结果。

import random
from copy import deepcopy

a = []

for i in range(15):
    a.append(random.randint(0, 100))

b = a[0:10]
c = a[10:]
b.sort(reverse=True)
c.sort()
a = b + c
print(a)

# a = []
# b = []
# c = []
#
# for i in range(15):
#     a.append(random.randint(0, 100))
# print(a)
# b = deepcopy(a[0:10])
# c = deepcopy(a[10:])
# b.sort(reverse=True)
# c.sort()
# a = b + c
# print(a)

# 4、s="hello world",去重并进行升序排序输出

# s = "hello world"
# b = []
# c = ''
# for i in s:
#     if ord(i) not in b:
#         b.append(ord(i))
#     if i == s[-1]:
#         b.sort()
#
# for i in b:
#     c += chr(i)
# print(c)
