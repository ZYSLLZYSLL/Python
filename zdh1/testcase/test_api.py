#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/28 17:22
# @Author : ZY
# @File : test_api.py
# @Project : zdh1
import pytest


class TestApi:

    @pytest.mark.parametrize('name,age', [['张三', '22'], ['李四', '21']])
    def test_01_baili(self, name, age):
        print('测试百里')
        print(name, age)


if __name__ == '__main__':
    pytest.main()
