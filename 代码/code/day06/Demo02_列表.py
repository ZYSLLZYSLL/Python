#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 10:23
# @Author : ZY
# @File : Demo02_列表.py
# @Project : code

"""
    列表（list,数组):以中括号为边界，以逗号隔开的数据（各种类型）
    特点：
        1，有序的
        2，可变的
        3，支持索引
        4，支持切片
"""

a = [1, True, None, [1, 2, 3], 'abc', (1, 2, 3), {'a': 1}, {1, 2, 3}, 1.23]
for i in a:
    print(f'{type(i)}-->{i}')
# 索引
print(a[3])

# 切片
print(a[::-1])
