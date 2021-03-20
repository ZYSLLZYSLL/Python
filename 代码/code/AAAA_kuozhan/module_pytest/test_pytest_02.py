#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 17:31
# @Author : ZY
# @File : test_pytest_02.py
# @Project : code
import allure
import pytest

"""
    blocker　   阻塞缺陷（功能未实现，无法下一步）
    critical　　严重缺陷（功能点缺失）
    normal　　  一般缺陷（边界情况，格式错误）
    minor　     次要缺陷（界面错误与ui需求不符）
    trivial　　 轻微缺陷（必须项无提示，或者提示不规范
"""

@allure.severity('normal')  # 等级
# 记录执行过程/步骤
@allure.step('打印了文字')
def test_01():
    # 文字描述
    allure.attach('这是用来打印的', '描述：')
    # 图片描述
    allure.attach.file('./output/2020121610241935da.jpg', '图片', attachment_type=allure.attachment_type.JPG)
    # allure.attach.file('./output/2020121610241935da.jpg', '图片', allure.attachment_type.JPG)
    print("\n这是test_pytest_02里面的test_01")


if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir=./output/reports', '--clean-alluredir'])
