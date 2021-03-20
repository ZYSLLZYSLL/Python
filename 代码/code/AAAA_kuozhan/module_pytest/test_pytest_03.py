#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 9:35
# @Author : ZY
# @File : test_pytest_03.py
# @Project : code

# 用例运行级别
"""
    模块级 setup_module和teardown_module，开始于模块始末（不能在类里写）
    类级  setuo_class和teardown_class，开始于类前后
    函数级 setup_function和teardown_function开始于函数始末（不能在类里写）
    方法级 setup_method和teardown_method 开始于方法始末
    类里面的 setup和teardown 开始于方法始末
"""
import pytest


# def setup_module():
#     print('\n__这是模块的开始__')
#
#
# def teardown_module():
#     print('\n__这是模块的结束__')
#
#
# def setup_function():
#     print('\n__这是函数的开始__')
#
#
# def teardown_function():
#     print('\n__这是函数的结束__')


# @pytest.mark.usefixtures('init')

# @pytest.mark.smoke
@pytest.mark.usefixtures('init_function')
def test_01():
    print("\n这是test_pytest_03里面的test_01")


# @pytest.mark.usefixtures('init_class')
# @pytest.mark.smoke
class Testclass():
    # def setup_class(self):
    #     print('\n__这是类的开始__')
    #
    # def teardown_class(self):
    #     print('\n__这是类的结束__')
    #
    # def setup(self):
    #     print('\n__这是方法级的开始__')
    #
    # def teardown(self):
    #     print('\n__这是方法级的结束__')
    a = 1

    # @pytest.mark.skipif(condition=1 < 2, reason='有条件跳过')
    # @pytest.mark.skipif(1 < 2, reason='有条件跳过')
    # @pytest.mark.skip('跳过')
    def test_02(self):
        print("\n这是test_pytest_03里面的test_02")

    def test_03(self):
        # if 2 > 1:
        #     pytest.skip('跳过')
        print("\n这是test_pytest_03里面的test_03")

        import pytest

        # def setup_module():
        #     print('\n__这是模块的开始__')
        #
        #
        # def teardown_module():
        #     print('\n__这是模块的结束__')
        #
        #
        # def setup_function():
        #     print('\n__这是函数的开始__')
        #
        #
        # def teardown_function():
        #     print('\n__这是函数的结束__')

        def test_01():
            print("\n这是test_pytest_03里面的test_01")

        class Testclass():
            # def setup_class(self):
            #     print('\n__这是类的开始__')
            #
            # def teardown_class(self):
            #     print('\n__这是类的结束__')
            #
            # def setup(self):
            #     print('\n__这是方法级的开始__')
            #
            # def teardown(self):
            #     print('\n__这是方法级的结束__')

            def test_02(self):
                print("\n这是test_pytest_03里面的test_02")

            def test_03(self):
                print("\n这是test_pytest_03里面的test_03")
