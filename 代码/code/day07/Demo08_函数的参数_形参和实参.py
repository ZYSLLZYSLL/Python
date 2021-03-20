#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 16:35
# @Author : ZY
# @File : Demo08_函数的参数_形参和实参.py
# @Project : code

# 请用函数完成两数的和

# def num(a, b):  # 形参
#     print(a + b)
#
#
# num(10, 20)  # 实参
# num('123', '456')  # 123456


# return 返回   功能1，返回值给调用者  2，结束函数

# def num1(a, b):  # 形参
#     print(a + b)
#     return (a + b)
#
#
# print(num1(1, 1) * 3)

# 使用函数，求三数之和，三数平均数
def avg(a, b, c):
    print(f'{a}+{b}+{c}={a + b + c}')
    return (a + b + c)


print('三数平均数为', avg(1, 2, 3) / 3)
