#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/20 16:37
# @Author : ZY
# @File : test_01.py
# @Project : jie_ko
import pytest
import requests


def test_01(z_m):
    res, key, chars = z_m
    print(res.text)
    assert chars[1] in res.text


# def test_02(m_z):
#     res, key, telecodes = m_z
#     print(res.text)
#     assert telecodes[0] in res.text


if __name__ == '__main__':
    pytest.main(["-s"])
