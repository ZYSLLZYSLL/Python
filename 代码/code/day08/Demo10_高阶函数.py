#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/15 11:44
# @Author : ZY
# @File : Demo10_高阶函数.py
# @Project : code

# ************************  高阶函数  ************************

# map() 依次将列表中的每个数据传入到函数中运行
a = [1, 2, 3, 4, 5, 6]


def aa(x):
    return x ** 2


b = list(map(aa, a))
print(b)

# filter() 过滤
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def bb(x):
    return x % 2 == 0


res = list(filter(bb, c))
print(res)
