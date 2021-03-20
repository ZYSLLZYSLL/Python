#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 20:33
# @Author : ZY
# @File : Demo08_列表_删除列表中所有1和5.py
# @Project : code

# 需求：删除列表中所有的1和5
b = []
a = [1, 2, 3, 4, 5, 1, 5]
for i in a:
    if (i == 1) or (i == 5):
        pass
    else:
        b.append(i)
print(b)

