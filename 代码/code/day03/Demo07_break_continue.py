#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 16:49
# @Author : ZY
# @File : Demo07_break_continue.py
# @Project : code

# break  结束循环
a = 0
while True:
    a += 1
    if a == 100:
        print(a)
        break

print("*"*100)
# continue  结束本次循环，开始下次循环
a = 0
while True:
    a += 1

    if a == 10:
        continue
    if a == 13:
        break
    print(a)
