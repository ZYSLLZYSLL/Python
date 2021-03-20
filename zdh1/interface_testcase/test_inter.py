#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/23 16:19
# @Author : ZY
# @File : test_login.py
# @Project : zdh1
import pytest

def test_04_func():
    print('函数')

class Testlogin:
    @pytest.mark.smoke
    def test_03_bowen(self):
        print('测试博文')
