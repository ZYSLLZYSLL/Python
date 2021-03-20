#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 11:23
# @Author : ZY
# @File : Demo04_列表常用操作_判断.py
# @Project : code

# 返回True 或者 False
# 也可以判断字符串的内容

a = [1, True, None, [1, 2, 3], 'abc', (1, 2, 3), {'a': 1}, {1, 2, 3}, 1.23, 'abc']

# (内容 in 列表)
print(1 in a)  # True

# (内容 not in 列表)
print('abc' not in a)  # False
