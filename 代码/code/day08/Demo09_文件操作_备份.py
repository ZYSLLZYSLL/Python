#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 17:17
# @Author : ZY
# @File : Demo09_文件操作_备份.py
# @Project : code

"""
    需求：用户输入当前目录下任意文件名，
    程序完成对该文件的备份功能(备份文件名为xx[备份]后缀，例如：test[备份].txt)。
"""
a = input('请输入你要备份的文件名：')
b = a.find('.')

name = a[:b] + '备份' + a[b:]

r_a = open(a, 'rb')
w_a1 = open(name, 'wb')

while True:
    con = r_a.read()
    if len(con) == 0:
        break
    w_a1.write(con)

w_a1.close()
r_a.close()