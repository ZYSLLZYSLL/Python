#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 19:01
# @Author : ZY
# @File : Demo10_不使用set(),完成去重功能.py
# @Project : code

# 不使用set(),完成去重功能，例[1,2,3,1,2,3]-->[1,2,3]
a = [1, 2, 3, 1, 2, 3]
a = {i: j for j, i in enumerate(a)}
a = [i for i in a.keys()]
print(a)


a = [1, 2, 3, 1, 2, 3]
print([i for i in {i: j for j, i in enumerate(a)}.keys()])


a = [1, 2, 3, 1, 2, 3]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
