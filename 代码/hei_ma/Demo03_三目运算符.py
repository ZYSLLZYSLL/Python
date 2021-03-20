#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 15:50
# @Author : ZY
# @File : Demo03_三目运算符.py
# @Project : code


"""
    格式：
    条件成立执行的语句 if 条件 else 条件不成立执行的语句
"""
"""
    需求：
        有两个变量比较大小，如果变量1大于变量2 执行 变量1 - 变量2 否则 变量2 - 变量1
"""

variable1 = int(input("请输入变量1:"))
variable2 = int(input("请输入变量2:"))

variable3 = (variable1 - variable2) if variable1 > variable2 else (variable2 - variable1)

print(variable3)
