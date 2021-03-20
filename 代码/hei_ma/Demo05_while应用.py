#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 16:41
# @Author : ZY
# @File : Demo05_while应用.py
# @Project : code

# 需求：1-100 累加和

i = 0
count = 1

while count <= 100:
    i += count
    count += 1

print(i)

# 1-100里偶数的累加和，即2+4+6+8……，

i = 0
count = 1
while count <= 100:
    if count % 2 == 0:
        i += count
    count += 1

print(i)


i = 0
count = 2
while count <= 100:
    i += count
    count += 2

print(i)
