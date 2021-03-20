#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 10:36
# @Author : ZY
# @File : Demo05_递归.py
# @Project : code


# 需求：3以内数字累加和

def num1(a):
    if a == 1:
        return 1
    sum = a + num1(a - 1)

    return sum


print(num1(3))


# def num(a):
#     print(a)
#     if a == 3:
#         return 3
#     result = a + num(a + 1)
#     return result
#
#
# print(num(1))
