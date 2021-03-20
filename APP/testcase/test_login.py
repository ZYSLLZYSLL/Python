#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 11:01
# @Author : ZY
# @File : test_login.py
# @Project : APP
import time

from appium import webdriver
import pytest
from pageObject.riLi import CalendarPage
from pageObject.woDe import MyPage
from pageObject.loginPage import LoginPage
from common.basePage import BasePage



# @pytest.mark.usefixtures('login')
class TestLogin:
    # def duix(self, init):
    #     self.driver = init
    #     self.CP = CalendarPage(self.driver)
    #     self.LP = LoginPage(self.driver)
    #     self.MP = MyPage(self.driver)

    # 正常登录,正确的账号，正确的密码
    # def test_login_sucess(self, login):
    #     LP, MP, CP, driver = login
    #     # # self.duix(init)
    #     # # 1，进入日历界面
    #     # self.CP.accept()  # 同意协议
    #     # # 2，进入到我的界面
    #     # self.MP.click_My()  # 点我的
    #     # # 3，点击未登录
    #     # self.MP.click_login_button()  # 点击 登录
    #     # # 4，输入用户名密码点击登录
    #     # self.LP.click_password_button()  # 选择密码验证按钮
    #     LP.input_username_password("15239938038", "bowen123456")  # 输入账号密码
    #     LP.click_protocol_button()  # 勾选同意协议
    #     LP.click_Login_buttor()  # 点击登录按钮
    #     # 5，断言获取用户名和预期结果是否相同
    #     assert MP.get_username_text() == "博文智生"

    # 异常登录，正确的账号，错误的密码
    def test_login_password_error(self, login):
        LP, MP, CP, driver = login
        # # 1，进入日历界面
        # self.CP.accept()  # 同意协议
        # # 2，进入到我的界面
        # self.MP.click_My()  # 点我的
        # # 3，点击未登录
        # self.MP.click_login_button()  # 点击 登录
        # # 4，输入用户名密码点击登录
        # self.LP.click_password_button()  # 选择密码验证按钮
        LP.input_username_password("15239938038", "bowen12345")  # 输入账号密码
        LP.click_protocol_button()  # 勾选同意协议
        LP.click_Login_buttor()  # 点击登录按钮
        # 5，断言获取用户名和预期结果是否相同
        # print(LP.check_agreement_toast())
        time.sleep(1)
        assert "账号" in LP.check_agreement_toast()
        # assert "账号" in driver.find_element_by_xpath("//*[contains(@text,'账号密码不正确')]").text
        # assert "账号" in self.LP.check_agreement_toast()
        # 截图
        # time.sleep(2)
        # self.screenshort("正确账号错误密码")
        # BasePage(driver).screenshort("正确的账号错误的密码")
        # driver.save_screenshot("../output/images/正确的账号错误的密码.png")
        # self.driver.get_screenshot_as_file("../output/images/正确的账号错误的密码1.png")


