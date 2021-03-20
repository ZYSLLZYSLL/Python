#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 15:32
# @Author : ZY
# @File : Demo02_猜拳游戏_随机数.py
# @Project : code


import random

Computer = random.randint(0, 2)

Player = int(input("玩家请出拳头：(0-石头，1-剪刀，2-布)："))
# Computer = 1
print(f"电脑出的是{Computer}")
if (Player == 0 and Computer == 1) or (Player == 1 and Computer == 2) or (Player == 2 and Computer == 0):
    print("玩家获胜！！！烟花，烟花，烟花")
elif Player == Computer:
    print("平局")
else:
    print("电脑获胜")

