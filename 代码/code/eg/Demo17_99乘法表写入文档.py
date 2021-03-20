#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 14:15
# @Author : ZY
# @File : Demo17_99乘法表写入文档.py
# @Project : code

# 需求：99乘法表写入文档中
a = open('a.txt', 'w', encoding='utf-8')
for i in range(1, 10):
    for j in range(1, i + 1):
        a.write(f'{j}*{i}={j * i}\t')
    a.write('\n')
a.close()
