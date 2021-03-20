#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 16:34
# @Author : ZY
# @File : test_pytest_05.py
# @Project : code
"""
    参数化
"""
import pytest


@pytest.mark.parametrize('a,b', [[1, 2], [3, 4]])  # a序列名称
def test_01(a, b):
    print(a, b)


@pytest.mark.parametrize('a', [[1, 2]])  # a序列名称
def test_02(a):
    print(a)
