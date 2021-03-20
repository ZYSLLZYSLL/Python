#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/9 13:57
# @Author : ZY
# @File : Demo01_for_嵌套.py
# @Project : code

for i in 'ZhouYu':  # 可迭代：取完之后不会再取
    print(i)

for i in 'ZhouYu':
    print('周宇')
'''
    内置函数 range(起始值，结束值，步进值)
    
    只有一个值时：range(结束值)       例如：range(10)    范围是0-9
    只有两个值时：range(起始值，结束值)       例如：range(1，10)    范围是1-9
    有三个值时：range(起始值，结束值，步进值)       例如：range(1，10，2)    范围是1，3，5，7，9
'''

for i in range(100):
    print(i)

print("*" * 100)

a = range(100)
print(a)

print("*" * 100)

# 1-100之和
i = 0
for count in range(1, 101):
    i += count
print(i)

# 1-100偶数之和
i = 0
for count in range(0, 101, 2):
    i += count
print(i)

"""
1,需求：打印星号（正方形）
*****
*****
*****
*****
*****
"""
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end='')
    print()

print("+" * 20)
"""
1,需求：打印星号（梯形）
*****
 *****
  *****
   *****
    *****
"""
for i in range(1, 6):
    for j in range(1, i):
        print(" ", end='')
    for j in range(1, 6):
        print("*", end='')
    print()

print("+" * 20)
"""
1,需求：打印星号（正方形）
*
**
***
****
*****
"""
for i in range(1, 6):
    for j in range(0, i):
        print("*", end='')
    print()

print("+" * 20)

# 9*9乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}\t", end="")
    print()

for i in range(10):
    print(i)
    if i == 3:
        break

for i in range(10):
    if i == 3:
        continue
    print(i)

print("-"*60)

'''
只要不被break,就执行else
while...else
for...else
'''

