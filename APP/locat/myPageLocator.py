#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:42
# @Author : ZY
# @File : myPageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class MyPageLocator:
    """
        我的页面元素
    """
    # 点击我的
    MyLocator = (By.ID, "com.tal.kaoyan:id/mainactivity_button_mysefl")
    # 点击登录
    loginLocator = (By.ID, "com.tal.kaoyan:id/activity_usercenter_username")
    # 获取用户名
    usernameTextLocator = (By.ID, "com.tal.kaoyan:id/activity_usercenter_username")

