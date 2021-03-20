#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 10:23
# @Author : ZY
# @File : test_pytest_04.py
# @Project : code


# from time import *
#
# def countT(s):
#     def t():
#         st = time()
#         s()
#         e = time()
#         print(f'时间{e - st}')
#
#     print(f'aa')
#     print(t)
#     return t
#
#
# @countT
# def h():
#     sleep(3)
#
# h()

"""
    打标签
        1，先在pytest.ini文件中配置
            [pytest]
            markers =
                smoke:冒烟测试
        2，使用pytest中装饰器来装饰测试用例
            @pytest.mark.smoke
        3，使用命令行pytest -m +标签名来执行测试用例
            pytest -m smoke
"""

"""
    配置文件conftest的配置和测试夹具fixture
"""



















