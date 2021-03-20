#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/24 14:15
# @Author : ZY
# @File : demo.py
# @Project : zdh1

f = open('a.txt', 'r', encoding='utf-8')
a = 0
for i in f.readlines():
    if (i.startswith('#')) or (i == '\n'):
        a += 1
print(a)
f.close()


# import re
#
# f = open('a.txt', 'r')
#
# a = re.findall("^#.*", f.readline(), re.S)
# print(a)
# f.close()
