#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:42
# @Author : ZY
# @File : calendarPageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class CalendarPageLocator:
    """
        首页元素
    """
    # 点确定
    acceptLocator = (By.ID, "com.tal.kaoyan:id/tip_commit")
    # 点广告X
    x1Locator = (By.ID, "com.tal.kaoyan:id/view_wemedia_cacel")
    # 点X
    x2Locator = (By.ID, "com.tal.kaoyan:id/kaoyan_home_schtip_close")
    # # 点击我知道了
    # iknowLocator = (By.ID, "com.tal.kaoyan:id/tv_ok")
    # # 同意权限
    # tongYiLocator = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    # # 点击跳过
    # tiaoGuoLocator = (By.ID, "com.tal.kaoyan:id/tv_skip")
