#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 17:02
# @Author : ZY
# @File : Demo08_文件操作_追加.py
# @Project : code

# f = open('a.txt', 'a', encoding='utf-8')
#
# f.write('\n周宇')
# f.close()

# 图片
f = open('a.png', 'rb')  # 把图片a用读打开
w = open('b.png', 'wb')  # 把图片b用写打开
fr = f.read()  # 读出图片a的二进制
w.write(fr)  # 把图片a的二进制写到b里面
w.close()  # 关闭写
f.close()  # 关闭读
