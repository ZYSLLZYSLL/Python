#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 9:08
# @Author : ZY
# @File : Demo01_类型强制转换.py
# @Project : code

# int(X)


# 将浮点数转换成整数

x = 1.1
x = int(x)
print(x)
print(type(x))

# 将进制数装换成十进制(0X十六进制，0B是二进制，0O是八进制)

x = 0x10
x = int(x)
print(x)
print(type(x))

x = 0b10
x = int(x)
print(x)
print(type(x))

x = 0o10
x = int(x)
print(x)
print(type(x))

# float(x)
x = 0o10
x = float(x)
print(x)
print(type(x))

# str(X) 指任何数据类型--连列表的格式都转化成字符串
a = [1, 2, 3, "123"]
a = str(a)
print(a)
print(type(a))

# eval(x) 值找出字符串中有效的表达式
a = '[1, 2, 3, "123"]'
a = eval(a)
print(a)
print(type(a))

a = '1+1'
a = eval(a)
print(a)
print(type(a))

# tuple(X)元组  指的是序列（列表，集合，元组，字符串，字典）

a = [1, 2, 3, "123"]
a = tuple(a)
print(a)
print(type(a))

a = "123"
a = tuple(a)
print(a)
print(type(a))

# list()
a = "123"
a = list(a)
print(a)
print(type(a))

# set()
a = "123"
a = set(a)
print(a)
print(type(a))
