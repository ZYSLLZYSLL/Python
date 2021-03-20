#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 9:44
# @Author : ZY
# @File : riLi.py
# @Project : APP

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 日历
from locat.calendarPageLocator import CalendarPageLocator as loc
from common.basePage import BasePage


class CalendarPage(BasePage):
    """
        日历页操作内容
    """

    # 同意协议
    def accept(self):
        self.click_element(loc.acceptLocator, "首页-同意协议")
        self.click_element(loc.x1Locator, "首页-点击广告X")
        self.click_element(loc.x2Locator, "首页-点击日程X")
        # self.click_element(loc.iknowLocator, "首页-点击我知道了")
