#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 10:01
# @Author : ZY
# @File : Demo02_运算符.py
# @Project : code

# 算数运算符 ：+ - * / // % **
# 除
print(7 / 3)
# 整除
print(7 // 3)
# 取余
print(7 % 3)
# 次方
print(7 ** 3)

print('*' * 100)
# 赋值运算符
# 多变量赋值--赋不同值
a, b, c = 1, 2, 3
print(a, c, b)

print('*' * 100)

# --赋相同值
a = b = c = 1
print(a, c, b)

print('*' * 100)
# 需求:a=1,b=2 将a,b两值互换
# 第一种，找个容器
a = 1
b = 2
c = a
a = b
b = c
print(a, b)

# 第二中，python特有的
a = 1
b = 2
a, b = b, a
print(a, b)

print('*' * 100)
# 复合赋值运算符

# 比较运算符
print(2 > 1)  # True
print(0 < 3 < 5)  # true
print('a' == 'a')  # True
print('a' != 'a')  # False
print(bool(0))  # False
print(bool(1))  # True

# 逻辑运算符

print(bool(0 and 1))  # False
