#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 11:16
# @Author : ZY
# @File : Demo05_enumerate_枚举.py
# @Project : code

# enumerate（序列,起始值(默认从0开始)）  枚举 迭代器

for i, j in enumerate('abcdefg'):
    print(i, j)

# for i, j in enumerate('abcdefg', start=10):
#     print(i, j)
