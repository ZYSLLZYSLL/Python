#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 15:03
# @Author : ZY
# @File : Demo_.csv.py
# @Project : code

import csv

"""
    写，普通写
"""

# header = ['id', 'name', 'age']
#
# values = [
#     (1, '周宇', 21),
#     (1, 'wang', 22)
# ]
#
# # with 上下文管理器，自带打开关闭
# with open('test.csv', 'w', newline='', encoding='utf-8') as f:
#     # f = open('test.csv', 'w', newline='', encoding='utf-8')
#     # 创建写入对象
#     writer = csv.writer(f)
#     # 写入一行、
#     writer.writerow(header)
#     # 写入多行
#     writer.writerows(values)

"""
    写，字典写入
"""
# header = ['id', 'name', 'age']
#
# values = [
#     {'id': 1, 'name': '周宇', 'age': 21},
#     {'id': 1, 'name': '周宇', 'age': 21},
# ]
# with open("test.csv", 'w', newline="") as f:
#     # 创建写入对象
#     writer = csv.DictWriter(f, header)
#     # 写入头部
#     writer.writeheader()
#     # 写入一行
#     writer.writerow({'id': 3, 'name': 'laowang', 'age': 33})
#     # 写入多行
#     writer.writerows(values)

"""
    读，以文本方式读取
"""

# with open('test.csv','r',encoding='utf-8') as f:
#     reader = csv.reader(f)
#     # print(reader)  # <_csv.reader object at 0x0000022C654FFAC8>
#     # 第一种取值的方法,一次取一个值
#     # titles = next(reader)
#     # print(titles)
#
#     # 第二种取值方法，生成一个列表
#     # print(list(reader))
#
#     # 第三种取值方法
#     for i in reader:
#         print(i)


"""
    读，以字典方式读取
"""
with open('test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)  # 一个字典
        print(i['name'])  # 字段的值
