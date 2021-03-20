#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 9:24
# @Author : ZY
# @File : Demo02_集合的常见操作_删除.py
# @Project : code

# remove(数据)，删除集合中的指定数据，如果数据不存在则 报错。
# a = {3, 4, 5, '周', '宇'}
# a.remove(4)
# print(a)  # {3, 5, '周', '宇'}

# discard(数据) 删除集合中的指定数据，如果数据不存在 不会报错。
# a = {3, 4, 5, '周', '宇'}
# a.discard('d')
# print(a)

# pop() 随机删除集合中一个数据，并返回该数据
a = {3, 4, 5, '周', '宇'}
b = a.pop()
print(a)  # {4, 5, '周', '宇'}
print('删除了', b)  # 删除了 3
