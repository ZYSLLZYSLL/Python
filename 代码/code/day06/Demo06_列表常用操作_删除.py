#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 11:41
# @Author : ZY
# @File : Demo06_列表常用操作_删除.py
# @Project : code

# del 列表
# a = [1, [1, 2, 3], 1.23, 'abc']
# del a
# print(a)  # 出异常，报错

# del 列表[位置]
# 删除指定内容
# a = [1, [1, 2, 3], 1.23, 'abc']
# del a[1]
# print(a)

# pop(下标) 删除指定下标的数据，并返回该数据,不带下标默认删除最后一个
# a = [1, [1, 2, 3], 1.23, 'abc']
# a.pop(1)
# print(a)

# remove(字符) 移除列表中某个数据的第一个匹配项
# a = [1, [1, 2, 3], 1.23, 'abc']
# a.remove('abc')
# print(a)

# 需求：删除列表中所有的1和5
b = []
a = [1, 2, 3, 4, 5, 1, 5]
for i in a:
    if (i == 1) or (i == 5):
        pass
    else:
        b.append(i)
print(b)

# clear() 清空列表
a = [1, [1, 2, 3], 1.23, 'abc']
print(a)
a.clear()
print(a)

