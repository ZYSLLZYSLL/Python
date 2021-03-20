#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/6 11:29
# @Author : ZY
# @File : Demo01_变量和注释的使用规则.py
# @Project : code

# 单行注释
# 注释的作用：对代码解释说明
"""
多行注释
Ctrl+/ 快捷单行注释
"""
'''
多行注释
'''
# print(12)

'''
常量：1 2 3 4 字符串 浮点数  空值 布尔值（True False）
定义：程序运行时，内容不发生改变的量叫常量、

变量：x y
定义：程序运行时，内容发生改变的量叫变量
'''
# x = 1
# print(x)
# x = 100
# print(x)

x = 1

while True:
    x = x + 1
    print("这是第", int(x), "次打印")
    if x == 1000:
        break
