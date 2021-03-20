#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 20:06
# @Author : ZY
# @File : Demo07_列表_办公室.py
# @Project : code

# 需求：有三个办公室，8位老师，8位老师随机分配到3个办公室

import random  # 导入包

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 8个老师
b = [[], [], []]  # 三个办公室


random.shuffle(a)  # 随机打乱a的顺序

for i in a:
    num = random.randint(0, 2)  # 0-2的随机数
    b[num].append(i)
# else:  # 只是降低一般的概率，并不能解决
#     c = tuple(b)
#     if (len(c[0]) == 0) or (len(c[1]) == 0) or (len(c[1]) == 0):
#         for i in a:
#             num = random.randint(0, 2)  # 0-2的随机数
#             b[num].append(i)

print(b)
