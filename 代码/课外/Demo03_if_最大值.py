#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 16:09
# @Author : ZY
# @File : Demo03_if_最大值.py
# @Project : code

# 要求输入三个整数，求最大值
a1 = int(input("请输入第一个数字："))
a2 = int(input("请输入第二个数字："))
a3 = int(input("请输入第三个数字："))

print(f"您输入是数字是:{a1} {a2} {a3}")
if a1 < a2:
    a1, a2 = a2, a1
if a1 < a3:
    a3, a1 = a1, a3

print(f"最大数是{a1}")
