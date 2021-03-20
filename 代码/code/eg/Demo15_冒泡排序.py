#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 9:07
# @Author : ZY
# @File : Demo15_冒泡排序.py
# @Project : code

# 两个两个对比

"""
    1，比较相邻两个数据,如果第一个比第二个大，就交换两个数
    2，对每一个相邻的数做同样1的工作，这样从开始一队到结尾一队在最后的数就是最大的数。
    3，针对所有元素上面的操作，除了最后一个。
    4，重复1~3步骤，知道顺序完成。

    在一个长度为N的序列中，要遍历N-1次
    第一次需要比较N-1次，把最大或最小的数移到最后
    第二次比较N-1-1次，
    。。。
"""
# a = [10, 1, 35, 61, 89, 36, 55]
# a = [1, 3, 4, 2, 6, 8, 3, 4, 6, 8, 10, 79, 34]
#
# b = []
# for i in range(len(a) - 1):
#     for j in range(len(a) - (i + 1)):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#     if b == a:
#         print(a)
#         break
#     else:
#         b.clear()
#         for q in a:
#             b.append(q)


a = [1, 3, 4, 2, 6, 8, 3, 4, 6, 8, 10, 79, 34]

for i in range(len(a) - 1):
    b = 0
    for j in range(len(a) - (i + 1)):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            b += 1
    if b == 0:
        print(a)
        break



