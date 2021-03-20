#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 20:35
# @Author : ZY
# @File : Demo08_for...else.py
# @Project : code

set1 = "zhouyu"

for i in set1:
    if i == "o":
        # break
        continue
    print(i)
else:
    print("正常结束")
