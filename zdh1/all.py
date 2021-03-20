#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/23 16:42
# @Author : ZY
# @File : all.py
# @Project : zdh1
import os

import pytest

if __name__ == '__main__':
    pytest.main()
    # pytest.main(['-vs', './interface_testcase/test_inter.py::test_04_func'])
    # pytest.main(['-vs', './interface_testcase/test_inter.py::Testlogin::test_03_bowen'])
    # pytest.main(['-vs', './testcase', '-n=2'])
    # pytest.main(['-vs', './testcase', '--reruns=2'])

    # os.system('allure generate ./temp -o ./report --clean')

