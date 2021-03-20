#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 11:32
# @Author : ZY
# @File : Demo05_列表常用操作_增加.py
# @Project : code

# append(数据) 列表结尾追加数据
a = [1, [1, 2, 3], 1.23, 'abc']
a.append('周宇')
print(a)  #[1, [1, 2, 3], 1.23, 'abc', '周宇']

# extend(内容) 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表。
a = [1, [1, 2, 3], 1.23, 'abc']
a.extend("周宇")
print(a)  # [1, [1, 2, 3], 1.23, 'abc', '周', '宇']

# insert(位置，数据)
a = [1, [1, 2, 3], 1.23, 'abc']
a.insert(1,"周宇")
print(a)  # [1, '周宇', [1, 2, 3], 1.23, 'abc']
