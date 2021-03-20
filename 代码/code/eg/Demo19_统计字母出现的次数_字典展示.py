#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 14:41
# @Author : ZY
# @File : Demo19_统计字母出现的次数_字典展示.py
# @Project : code

# 统计每个字符出现的次数，并用字典展示

a = 'abcdefabcd'
c = {}

for i in a:
    c[i] = a.count(i)
print(c)
