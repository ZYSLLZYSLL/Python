#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 11:06
# @Author : ZY
# @File : Demo03_列表常用操作_查找.py
# @Project : code

a = [1, True, None, [1, 2, 3], 'abc', (1, 2, 3), {'a': 1}, {1, 2, 3}, 1.23, 'abc']
# index(数据，开始下标，结束下标) 返回指定内容的位置
# print(a.index(None))  # 2
# print(a.index(1))  # 0

# count() 统计指定数据出现的次数
# print(a.count("abc"))  # 2

# len() 统计列表长度
print(len(a))  # 10

