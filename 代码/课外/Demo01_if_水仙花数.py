#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 15:33
# @Author : ZY
# @File : Demo01_if_水仙花数.py
# @Project : code

"""
输入一个三位数，判断该数字是否是水仙花数，如果是，输出yes!，否则输出No!
提示：水仙花数：该数字的百位、十位、个数的立方和等于这个数本身。
三位的水仙花数共有4个：153，370，371，407；
"""
digital = int(input("请输入一个三位数："))

if 100 <= digital <= 999:
    bai = digital // 100
    shi = (digital % 100) // 10
    ge = digital % 10
    if bai ** 3 + shi ** 3 + ge ** 3 == digital:
        print("Yes!")
    else:
        print("No!")
else:
    print("请输入三位数的数字,不要输入其他位数的")

