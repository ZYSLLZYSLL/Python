#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 10:42
# @Author : ZY
# @File : Demo03.py
# @Project : code

# 只导入列表里面的
__all__ = ['name']

name = 1


def hanShu():
    print('周宇')


# print(__name__)

# 解决在其他模块执行的问题
if __name__ == '__main__':
    print('在本文件')
