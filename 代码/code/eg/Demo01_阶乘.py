#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 17:49
# @Author : ZY
# @File : Demo01_阶乘.py
# @Project : code

# 阶乘之和   一个范围的阶乘之和   1！+2！+3！+4！
# 1+1x2+1x2x3+1x2x3x4
# for
b = 0
for i in range(1, 101):
    a = 1
    for j in range(1, i + 1):
        a *= j
    b += a
print('for_100以内所有数的阶乘的和为', b)
print('-' * 100)

# while
b = 0
i = 1
while i <= 100:
    a = 1
    j = 1
    while j < (i + 1):
        a *= j
        j += 1
    b += a
    i += 1
print('while_100以内所有数的阶乘的和为', b)

# 这个也是
sum = 0
a = 1
for i in range(1, 6):
    a *= i
    sum += a
print(a)
