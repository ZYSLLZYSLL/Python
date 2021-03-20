#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/20 16:37
# @Author : ZY
# @File : test_01.py
# @Project : jie_ko
import pytest
import requests


def test_01(biaozhendianma):
    # res = requests.get(biaozhendianma[0], params=biaozhendianma[1])
    # print(res)
    assert "周" in biaozhendianma
    # print(biaozhendianma)


if __name__ == '__main__':
    pytest.main(["-s"])
