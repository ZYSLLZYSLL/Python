#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 15:42
# @Author : ZY
# @File : conftest.py
# @Project : APP
import time

from appium import webdriver
import pytest
from pageObject.riLi import CalendarPage
from pageObject.woDe import MyPage
from pageObject.loginPage import LoginPage
from dataDriver.yamlData import readYaml
from common.allPathSet import AllPathSet
import os
"""
    conftest夹具
"""



@pytest.fixture()
def login():
    driver = baseDriver()
    CP = CalendarPage(driver)
    LP = LoginPage(driver)
    MP = MyPage(driver)
    # self.duix(init)
    # 1，进入日历界面
    CP.accept()  # 同意协议
    # 2，进入到我的界面
    MP.click_My()  # 点我的
    # 3，点击未登录
    MP.click_login_button()  # 点击 登录
    # 4，输入用户名密码点击登录
    LP.click_password_button()  # 选择密码验证按钮
    yield LP, MP, CP, driver
    driver.close_app()


def baseDriver():
    # 构造参数
    desired_capabilities = AllPathSet.DEVICE_PATH
    # os.system("adb install ../app/com.tal.kaoyan_3.8.1_liqucn.com.apk")
    # time.sleep(10)
    # 向服务端发送连接信息
    driver = webdriver.Remote(AllPathSet.APPIUM_HTTP_PATH, desired_capabilities)
    driver.implicitly_wait(10)
    return driver
    # driver.close_app()
