#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 9:40
# @Author : ZY
# @File : loginPage.py
# @Project : APP

# 登录页
import time

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.basePage import BasePage
from locat.loginPageLocator import LoginPageLocator as loc


# 隐形等待 智能等待 一般不单独使用 每个操作大概分配几秒的样子
# driver.implicitly_wait(10)


class LoginPage(BasePage):
    """
        登录页操作内容
    """

    # def __init__(self, driver: Remote):
    #     self.driver = driver

    # 点击密码验证登录

    def click_password_button(self):
        self.click_element(loc.passwordButtonLocator, "登录页-点击使用密码验证登录")

    # 输入账号密码
    def input_username_password(self, user, password):
        self.input_element(user, loc.usernameLocator, "登录页-输入账号")
        self.input_element(password, loc.passwordLocator, "登录页-输入密码")

    # 勾选同意协议
    def click_protocol_button(self):
        self.click_element(loc.protocolLocator, "登录页-勾选同意协议")

    # 点击登录按钮
    def click_Login_buttor(self):
        self.click_element(loc.loginButtorLocator, "登录页-点击登录")

    # toast  模糊匹配: //*[contains(@text,'部分内容')]
    def check_agreement_toast(self):
        return self.get_element_text(loc.agreement_toastLocator, "登录页-toast文本")
