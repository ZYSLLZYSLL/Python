#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 9:46
# @Author : ZY
# @File : woDe.py
# @Project : APP

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locat.myPageLocator import MyPageLocator as loc
from common.basePage import BasePage


# 我的

class MyPage(BasePage):
    """
        我的页面操作内容
    """

    # 点我的
    def click_My(self):
        self.click_element(loc.MyLocator, "我的页面-点击我的")

    # 点击 登录
    def click_login_button(self):
        self.click_element(loc.loginLocator, "我的页面-点击未登录")

    def get_username_text(self):
        return self.get_element_text(loc.usernameTextLocator, "我的页面-验证登录名")
