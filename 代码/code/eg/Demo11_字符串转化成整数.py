#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 19:16
# @Author : ZY
# @File : Demo11_字符串转化成整数.py
# @Project : code

# 将字符串‘123’--->123，不使用int(),eval()
# b.find(a[i])  这句话的意思就是a里面的字符在b里面的下标位置
a = '123'
b = '0123456789'
c = 0
for i in range(len(a)):
    c += (b.find(a[i]) * 10 ** (len(a) - (i + 1)))
print(c)
print(type(c))
