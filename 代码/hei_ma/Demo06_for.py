#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 19:15
# @Author : ZY
# @File : Demo06_for.py
# @Project : code

set1 = "zhouyu"

for i in set1:
    print(i)

print("*" * 30)
# break
for i in set1:
    if i == "o":
        print("遇见o下面就不打印了")
        break
    print(i)

print("*" * 30)
# continue
for i in set1:
    if i == "o":
        print("遇见o就跳过")
        continue
    print(i)
