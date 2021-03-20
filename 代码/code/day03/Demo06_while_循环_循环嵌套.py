#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 15:42
# @Author : ZY
# @File : Demo06_while_循环_循环嵌套.py
# @Project : code

# 需求：求1-100之和
i = 0
count = 1
while count <= 100:
    i += count
    count += 1
print(i)

# 需求：求1-100,偶数之和之和
i = 0
count = 0
while count <= 100:
    i += count
    count += 2
print(i)

# 循环嵌套

a = 0
while a < 3:
    a += 1
    b = 0
    while b < 3:
        b += 1
        print("hello world")
    print("hello ZhouYu")
    print("*" * 20)
