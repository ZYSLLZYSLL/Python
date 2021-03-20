#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 19:04
# @Author : ZY
# @File : Demo05_排列.py
# @Project : code
# a,b,c三个元素有多少个排列组合 abc acb
# for
count = 0
for i in 'abc':
    for j in 'abc':
        for a in 'abc':
            if (i == j) or (j == a) or (i == a):
                continue
            else:
                print(i,j,a)
                count += 1
print(f'for_a,b,c三个元素有{count}种排列组合')

print('-' * 100)
# while
a = 'abc'
i = j = k = 0
while i < 3:
    while j < 3:
        while k < 3:
            if (i != j) and (j != k) and (i != k):
                print(a[i], a[j], a[k])
            k += 1
        j += 1
        k = 0
    i += 1
    j = 0
