#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 19:02
# @Author : ZY
# @File : Demo03_质数之和.py
# @Project : code

# 质数之和    质数  只能被自己和1整除的数叫质数 ts:2 3 5 7 11 13 17

# for

a = 0
b = 0
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            a = 1
    if a == 0:
        b += i
    else:
        a = 0
print('for_100以内所有质数的和为', b)


print('-' * 100)
# while

a = b = 0
i = 1

while i < 100:
    i += 1
    j = 2
    while j < i:
        if i % j == 0:
            a = 1
        j += 1
    if a == 0:
        b += i
    else:
        a = 0
print('while_100以内所有质数的和为', b)

b = 0
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        b += i

print('for_100以内所有质数的和为', b)
