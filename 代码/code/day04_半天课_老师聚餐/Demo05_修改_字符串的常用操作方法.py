#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/9 17:29
# @Author : ZY
# @File : Demo05_修改_字符串的常用操作方法.py
# @Project : code

# replace(’旧子串‘，’新子串‘，替换次数);替换
# a = 'hello world'
# print(a.replace('l', 'zy'))  # 把‘l’替换成'zy'，全部替换
# print(a.replace('l', 'zy', 2))  # 把‘l’替换成'zy'，替换两次
#
# print('-' * 100)

# split('分割字符'，分割符次数);分割
# a = 'ma welcome my home'
# print(a.split('m'))  # 列表类型 # 分割的字符前面如果没有字符，默认是空格字符

# join(字符串组成的序列);

# a = ['1', '2', '3', '4']
# print('-*-'.join(a))  # 把--放到a这个序列的字符串之间

# capitalize() 将字符串的首字符大写
# a = 'ma welcome my home'  # 将字符串的首字符大写
# print(a.capitalize())

# title() 将字符串中 每个单词 的 首字母 大写
# a = 'ma welcome my home'
# print(a.title())

# lower() 将字符串中的大写变小写
# a = 'ma wElcOme my hoMe'
# print(a.lower())

# upper() 将字符串中的小写变成大写
# a = 'ma wElcOme my hoMe'
# print(a.upper())  # 原来就是大写的不改变

# lstrip() 删除字符串中左边的空格（空白字符）
# a = '     ma wElcOme my hoMe        '
# print(a.lstrip())

# rstrip() 删除字符串中右边的空格（空白字符）
# a = '     ma wElcOme my hoMe        '
# print(a.rstrip())

# strip() 删除字符串中两边的空格（空白字符） 中间的字符无法删除
a = '     ma wElcOme my hoMe        '
# print(a.strip())
# print(a.strip(' e'))  # 将含有的字符删除,从两侧开始，遇见不包含的字符就停止

# ljust() 将字符串左对齐，数字指前多少个字符 不够的话用后面的字符填充
# a = 'ma wElcOme my hoMe'
# b = a.ljust(20,'.')
# print(b)

# rjust() 将字符串右对齐，数字指前多少个字符 不够的话用后面的字符填充
# a = 'ma wElcOme my hoMe'
# b = a.rjust(20,'.')
# print(b)

# center() 将字符串居中 不够的话用后面字符填充
# a = 'ma wElcOme my hoMe'
# b = a.center(20,'.')
# print(b)







