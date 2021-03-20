#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 8:59
# @Author : ZY
# @File : Demo01_集合.py.py
# @Project : code
"""
    集合（set):以大括号为边界，以逗号隔开的数据（各种类型）
    特点：
        1，无序的
        2，可变的
        3，不可重复的
        4，命名空集合时，需要用set(),不能用大括号'{}'
"""

# 无序,输入和输出的顺序不一样
# a = {3, 2, 5}
# print(a)  # {2, 3, 5}

# 不可重复的,自带去重功能
# a = {3, 2, 5, 5}
# print(a)  # {2, 3, 5}

# 命名空集合时，需要用set(),不能用大括号'{}'
# a = {}  # 这样的类型是字典，所以不能用 错误
# print(type(a))  # <class 'dict'>
#
# a = set()
# print(type(a))  # <class 'set'>
