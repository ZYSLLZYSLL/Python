#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 16:12
# @Author : ZY
# @File : test_sample.py
# @Project : code

import os
b = 'cc'
a = os.getcwd()
a = a+f'\\{b}'
print(a)
os.chdir(a)
print(os.getcwd())
