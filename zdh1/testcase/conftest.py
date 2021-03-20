#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/28 15:58
# @Author : ZY
# @File : conftest.py
# @Project : zdh1


"""
    @pytest.fixture装饰器
"""

import pytest



# @pytest.fixture(scope="", params="", autouse="", ids="", name="")
@pytest.fixture(scope="module", params=['第一次', '第二次', '第三次'], ids=['qqq', 'www', 'eee'], name='aaa')
def my_fixture(request):  # 这个方法名字可以随意取
    # return request.param
    print('\n这是前置的方法，可以实现部分以及全部用例的前置')
    yield request.param
    print('\n这是后置的方法，可以实现部分以及全部用例的后置')
