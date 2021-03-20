#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 17:06
# @Author : ZY
# @File : Demo08_元组.py
# @Project : code

'''
    元组（tuple):以小括号为边界，以逗号隔开的数据（各种类型）
    特点：
        1，有序的
        2，不可变的
        3，支持索引
        4，支持切片
'''
# a = (1,2,3)
# b = (1,2,3)
# print(id(a))
# print(id(b))

# index(内容) 查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index方法相同。
# a = (1,2,3)
# print(a.index(1))  # 0

# count(内容)：统计某个数据在当前元组出现的次数。
# a = (1, 2, 3, 1)
# print(a.count(1))

# len(元组)：统计元组中数据的个数。
a = (1, 2, 3, 1)
print(len(a))

