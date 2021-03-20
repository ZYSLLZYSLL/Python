#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/9 15:37
# @Author : ZY
# @File : Demo00_循环嵌套的一些题.py
# @Project : code

# 质数之和 (100之内)
# 阶乘之和 一个范围内阶乘和（100）
# 一个数的因数之和 键盘输入
# a,b,c三个元素有多少个排列组合


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

print('-' * 100)
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

print('-' * 100)
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
            if (i == j) or (j == a) or (i == a):
                continue
            else:
                print(a[i],a[j],a[k])



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
