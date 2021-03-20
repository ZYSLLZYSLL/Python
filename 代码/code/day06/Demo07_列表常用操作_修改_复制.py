#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 15:35
# @Author : ZY
# @File : Demo07_列表常用操作_修改_复制.py
# @Project : code

# 修改指定位置的数据
# a = [1, [1, 2, 3], 1.23, 'abc']
# a[1] = '周宇'
# print(a)

# 逆置：reverse()
# a = [1, [1, 2, 3], 1.23, 'abc']
# a.reverse()
# print(a)
# # print(a[::-1])

# 排序 sort() 默认升序
# a = [1, 3, 5, 8, 0, 3]
# a.sort()
# print(a)

# 降序
# a = [1, 3, 5, 8, 0, 3]
# a.sort(reverse = True)
# print(a)

# copy() 复制,浅复制
# a = [1, [1, 2, 3], 1.23, 'abc']
# b = a.copy()
# print(b)
# print(id(a[1]))
# print(id(b[1]))
# print(id(a[0]))
# print(id(b[0]))

# 二维数组
# a = [1, [1, 2, 3], 1.23, 'abc']
# print(a[1][2])

# 深复制：
# from copy import deepcopy
# a = [1, [1, 2, 3], 1.23, 'abc']
# b = deepcopy(a)
# print(id(a[1]))
# print(id(b[1]))
# print(id(a[0]))
# print(id(b[0]))
a = [1, [1, 2, 3], 1.23, 'abc']
b = a.copy()
b[1] = a[1].copy()
print(id(a[1]))
print(id(b[1]))
print(id(a))
print(id(b))

'''
    浅复制：对于可变类型没有完全复制
    深复制：全部复制
'''
