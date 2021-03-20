#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/14 17:33
# @Author : ZY
# @File : Demo14_文件备份.py
# @Project : code
"""
    需求：用户输入当前目录下任意文件名，
    程序完成对该文件的备份功能(备份文件名为xx[备份]后缀，例如：test[备份].txt)。
"""
a = input('请输入你要备份的文件名:')
b = a.rfind('.')

name = a[:b] + '[备份]' + a[b:]

r = open(a, 'rb')
w = open(name, 'wb')

a_r = r.read()
w.write(a_r)

w.close()
r.close()
