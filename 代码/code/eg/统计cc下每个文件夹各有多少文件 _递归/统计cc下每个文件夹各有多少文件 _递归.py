#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 13:24
# @Author : ZY
# @File : 统计cc下每个文件夹各有多少文件 _递归.py
# @Project : code

"""
# 需求：统计cc下每个文件夹各有多少文件  递归
cc
    a
        a.txt
        a.png
    b
        b.txt
        b.png
    c
        c.txt
        c.png
"""
import os


def c(mulu):  # mulu:目录

    num = 0
    b = os.getcwd() + f'\\{mulu}'  # b是刚才输入目录的根路径

    for i in os.listdir(mulu):  # 遍历目录下所有文件
        os.chdir(b)  # 切换到刚才的路径
        if os.path.isdir(i):
            c(i)
        else:
            num += 1
    else:
        print(f'{b}目录下有{num}个文件')


c('cc')

# import os
#
# def look(a):
#     c = 0
#     for i in os.listdir(a):
#         p = a+f"\\{i}"
#         if os.path.isdir(p):
#             look(p)
#         elif os.path.isfile(p):
#             c+=1
#     else:
#         print(a,c)
# look('cc')


# # 创建题意文件夹，文件
# os.makedirs('cc/a')
# os.makedirs('cc/b')
# os.makedirs('cc/c')
# f = open(r'cc\a\a.txt', 'w')
# f.close()
# f = open(r'cc\a\a.png', 'w')
# f.close()
# f = open(r'cc\b\b.txt', 'w')
# f.close()
# f = open(r'cc\b\b.png', 'w')
# f.close()
# f = open(r'cc\c\c.txt', 'w')
# f.close()
# f = open(r'cc\c\c.png', 'w')
# f.close()
