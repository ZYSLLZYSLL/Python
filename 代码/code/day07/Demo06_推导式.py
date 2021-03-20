#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 11:18
# @Author : ZY
# @File : Demo06_推导式.py
# @Project : code

# **************************************列表推导式
# 需求：创建一个0-10的列表

# for
# a = []
# for i in range(11):
#     a.append(i)
# print(a)

# 列表推导式
# print([i for i in range(11)])

# a = [i for i in range(11)]
# print(a)

# a = [(i, j) for i in range(11) for j in range(11)]
# print(a)

# 需求:创建一个A-Z的列表
# b = [chr(i) for i in range(65,91)]
# print(b)

# 需求：创建0-10的偶数列表

# **************************************集合推导式
# 需求:创建一个A-Z的列表
# b = {chr(i) for i in range(65,91)}
# print(b)

# **************************************字典推导式
a = ['a', 'b', 'c']
d = {j: i for i, j in enumerate(a)}
print(d)
