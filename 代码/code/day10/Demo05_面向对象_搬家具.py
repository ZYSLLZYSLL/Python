#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/15 16:47
# @Author : ZY
# @File : Demo05_面向对象_搬家具.py
# @Project : code

"""
需求
    将小于房子剩余面积的家具摆放到房子中
步骤分析
    需求涉及两个事物：房子 和 家具，故被案例涉及两个类：房子类 和 家具类。
"""

# class JiaJu():
#     def __init__(self, name, s):
#         self.name = name  # 家具名字
#         self.jiaJu_s = s  # 家具面积
#
#
# class FangZi():
#     def __init__(self, adds, s):
#         self.adds = adds  # 房子位置
#         self.jia_s = s  # 房子面积
#         self.jia_y_s = s  # 房子剩余面积
#         self.lieBiao = []
#
#     def __str__(self):
#         a = f'您的房子位于{self.adds}\n'
#         a += f'您房屋总面积为{self.jia_s}平方米\n'
#         a += f'您房屋剩余面积为{self.jia_y_s}平方米\n'
#         b = ''
#         if len(self.lieBiao) == 0:
#             b = '无'
#         else:
#             b = ','.join(self.lieBiao)
#         a += f'当前屋内已有家具都有:{b}\n'
#         return a
#
#     def add(self, ban):
#         if self.jia_y_s > ban.jiaJu_s:
#             self.jia_y_s -= ban.jiaJu_s
#             self.lieBiao.append(ban.name)
#         else:
#             print('房子面积不够大，换房子吧')
#
#
# jia = FangZi('北京', 120)
# jiaju = JiaJu('床', 30)
# jia.add(jiaju)
# print(jia)


"""
需求
    将小于房子剩余面积的家具摆放到房子中
步骤分析
    需求涉及两个事物：房子 和 家具，故被案例涉及两个类：房子类 和 家具类。
"""


class JiaJu():
    def __init__(self, name, s):
        self.name = name  # 家具名字
        self.jiaJu_s = s  # 家具面积


class FangZi():
    def __init__(self, adds, s):
        self.adds = adds  # 房子位置
        self.jia_s = s  # 房子面积
        self.jia_y_s = s  # 房子剩余面积
        self.lieBiao = []

    def __str__(self):
        a = f'您的房子位于: {self.adds}\n'
        a += f'您房屋总面积为{self.jia_s}平方米\n'
        a += f'您房屋剩余面积为{self.jia_y_s}平方米\n'
        b = ''
        if len(self.lieBiao) == 0:
            b = '无'
        else:
            b = ','.join(self.lieBiao)
        a += f'当前屋内已有家具都有:{b}\n'
        return a

    def add(self, ban):
        if self.jia_y_s > ban.jiaJu_s:
            self.jia_y_s -= ban.jiaJu_s
            self.lieBiao.append(ban.name)
        else:
            print('房子面积不够大，换房子吧')


aa = input('请输入您的房屋的位置:')
bb = int(input('请输入您访问的总面积'))
jia = FangZi(aa, bb)

while True:
    cc = input('请输入您要添置家具的名字:')
    dd = int(input('请输入您要添置家具的面积'))

    print()

    jiaju = JiaJu(cc, dd)
    jia.add(jiaju)
    print(jia)

    ee = input('请输入您还要继续添置家具吗？(Y/N)')

    if ee == 'N' or ee == 'n':
        break
