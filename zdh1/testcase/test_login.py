#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/23 16:19
# @Author : ZY
# @File : test_login.py
# @Project : zdh1
import pytest
import time


class Testlogin:

    @pytest.mark.skip(reason='这里是跳过的原因，只是说明一下')
    def test_01_baili(self):
        print('测试百里')

    a = 11

    @pytest.mark.skipif(a >= 10, reason='条件成立跳过')
    def test_02_bw(self):
        print('测试博文')

    @pytest.mark.run(order=1)  # 加标记，我希望这一个用例第一个执行
    @pytest.mark.usermanage
    def test_03_kd(self):
        print('测试开大')

    @pytest.mark.smoke
    def test_04_kf(self):
        print('测试开封')
