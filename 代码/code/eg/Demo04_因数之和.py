#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 19:03
# @Author : ZY
# @File : Demo04_因数之和.py
# @Project : code
# 一个数的因数之和  ts:6 1+2+3+6
# for
b = 0
a = int(input('请输入一个数字：'))
for i in range(1, a + 1):
    if a % i == 0:
        b += i
print(f'while_数字{a}的所有因数之和为{b}')

print('-' * 100)
# while
b = 0
i = 1
a = int(input('请输入一个数字：'))
while i <= a:
    if a % i == 0:
        b += i
    i += 1
print(f'for_数字{a}的所有因数之和为{b}')
