#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 9:08
# @Author : ZY
# @File : Demo16_选择排序.py
# @Project : code

# 一个和所有对比
"""
    1，在一个长度为 N 的无序数组中，第一次遍历 n-1 个数找到最小的和第一个数交换。
    2，第二次从下一个数开始遍历 n-2 个数，找到最小的数和第二个数交换。
    3，重复以上操作直到第 n-1 次遍历最小的数和第 n-1 个数交换，排序完成。
"""
a = [10, 1, 35, 61, 89, 36, 55]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)
