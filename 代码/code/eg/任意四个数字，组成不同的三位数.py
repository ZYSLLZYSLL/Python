#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/23 11:17
# @Author : ZY
# @File : 任意四个数字，组成不同的三位数.py
# @Project : code

values = input('请输入四位数字:')
if len(values) == 4:
    for i in values:
        for j in values:
            for k in values:
                print(i, j, k)
else:
    print("请输入四位数字，只能四位")
