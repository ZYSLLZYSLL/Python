#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 10:23
# @Author : ZY
# @File : Demo04_拆包.py
# @Project : code

# 元组的拆包
a, b, c = (10, 20, 30)  # 前面变量的个数要和元组的长度一样
print(c)  # 30

# 当不知道元组长度时可以用“*c”来拿走后面所有的数据，*c的类型是列表
a, b, *c = (10, 20, 30, 40, 50)
print(c)  # 30

# 字典的拆包
dict1 = {'name': '周宇', 'age': 20}
a, b = dict1    # 前面变量的个数要和字典键的个数一样，出来的是 键
print(a, b)
print(dict1[a], dict1[b])
