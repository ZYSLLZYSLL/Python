#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 10:03
# @Author : ZY
# @File : Demo03_os.py
# @Project : code

import os

# 输入终端命令
a = os.popen('ipconfig/all')
print(a.read())

# 获取当前所在位置
print(os.getcwd())

# 切换目录
# os.chdir('D:')
print(os.getcwd())

# 查看当前目录下所有文件
print(os.listdir('D:'))

# 删除文件
# os.remove('index.html')
print(os.listdir(r'..\day17'))  # 查看当前目录下所有文件

"""
    路径分割
"""
# 将路径与文件分割开,  不判断文件或文件夹
a = os.path.split(r'E:\新\软件测试\5.第五阶段\代码\code\dey17')
# ('E:\\新\\软件测试\\5.第五阶段\\代码\\code', 'day17')
print(a)

# 将路径与后缀名分割开,  不判断文件或文件夹
a = os.path.splitext(r'E:\新\软件测试\5.第五阶段\代码\code\dey17.py')
# ('E:\\新\\软件测试\\5.第五阶段\\代码\\code\\day17', '.py')
print(a)

# 将盘符与路径分割开,  不判断文件或文件夹
a = os.path.splitdrive(r'E:\新\软件测试\5.第五阶段\代码\code\dey17')
# ('E:', '\\新\\软件测试\\5.第五阶段\\代码\\code\\day17')
print(a)

"""
    判断文件
"""
# 判断是不是文件夹
a = os.path.isdir(r'E:\新\软件测试\5.第五阶段\代码\code\dey17')
print(a)  # True

# 判断是不是文件
a = os.path.isfile(r'/day17\__init__.py')
print(a)  # True

"""
    文件夹操作
"""
# 创建文件夹
# os.mkdir('a')
# print(os.listdir(r'E:\新\软件测试\5.第五阶段\代码\code\day17'))  # 查看路径下所有文件

# 删除空文件夹
# os.rmdir('a')
# print(os.listdir(r'E:\新\软件测试\5.第五阶段\代码\code\day17'))  # 查看路径下所有文件

# 创建递归文件夹
# os.makedirs(r'a\b\c')
# print(os.listdir(r'E:\新\软件测试\5.第五阶段\代码\code\day17'))  # 查看路径下所有文件

# 移除指定文件
# os.remove(r'a\b\a.txt')
# print(os.listdir(r'E:\新\软件测试\5.第五阶段\代码\code\day17'))  # 查看路径下所有文件

"""
    文件重命名
"""
# 单文件命名
# os.rename('a.py', 'a.txt')
# os.rename(r'a\b\c', r'a\b\d')

# 多文件改名
# os.renames(r'a\b\c', r'aa\bb\cc')



