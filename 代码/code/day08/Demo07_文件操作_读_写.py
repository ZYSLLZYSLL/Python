#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 15:25
# @Author : ZY
# @File : Demo07_文件操作_读_写.py
# @Project : code

"""
    写入文件
"""
#  encoding 可以把文件类型变成utf-8

# a = open("a.txt", "w", encoding="utf_8")  # 打开文件设置权限
# a.write('hello world\n')  # 默认不会换行 写入文件内容
# a.write('hello world\n')
# a.write('hello world\n')
# a.write('周宇\n')
# a.close() # 关闭并保存文件

# 需求：将数字1-100写入文档中，并换行
# a = open("a.txt", "w", encoding="utf_8")
# for i in range(101):
#     a.write(f'{i}\n')
# a.close()

# 需求：99乘法表写入文档中
# a = open('a.txt', 'w', encoding='utf-8')
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         a.write(f'{j}*{i}={j * i}\t')
#     a.write('\n')
# a.close()

"""
    读
"""
# 读文件，相对路径
# f = open('a.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

# 读文件，觉对路径
# f = open('E:\\新\\软件测试\\5.第五阶段\\代码\\code\\day08\\a.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

# 读文件，将特殊字符变为原生字符串 r""
# f = open(r'E:\新\软件测试\5.第五阶段\代码\code\day08\a.txt', 'r', encoding='utf-8')
# # f.read() 将文件中所有内容以字符串的形式读出来
# print(f.read())
# # f.readline() 将文件中所有内容以列表的形式读出来
# print(f.readline())
# # f.readline() 以字符串读出一行内容
# print(f.readline())
# f.close()


# 需求：统计文件中含有#开头的行和空行总共有多少行
count = 0

a = open('a.txt', 'r', encoding='utf-8')

for i in a.readlines():
    if i.startswith('#') or i == '\n':
        count += 1
print(count)
a.close()


count = 0

a = open('a.txt', 'r', encoding='utf-8')
b = a.readlines()
for i in range(len(b)):
    if b[i].startswith('#') or b[i] == '\n':
        count += 1
print(count)
a.close()
