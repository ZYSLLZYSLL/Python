#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 9:05
# @Author : ZY
# @File : 一行代码计算1到100的和.py
# @Project : code
print(sum([i for i in range(1, 101)]))

print((lambda i: sum(i))(i for i in range(1, 101)))

print(sum(range(1, 101)))
