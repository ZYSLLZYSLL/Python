#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:37
# @Author : ZY
# @File : loginPageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class LoginPageLocator:
    """
        登录页元素
    """
    # 选择密码验证按钮
    passwordButtonLocator = (By.ID, "com.tal.kaoyan:id/login_code_touname")
    # 账号
    usernameLocator = (By.ID, "com.tal.kaoyan:id/login_email_edittext")
    # 密码
    passwordLocator = (By.ID, "com.tal.kaoyan:id/login_password_edittext")
    # 同意协议
    protocolLocator = (By.ID, "com.tal.kaoyan:id/login_treaty_checkbox_password")
    # 登录按钮
    loginButtorLocator = (By.ID, "com.tal.kaoyan:id/login_login_btn")
    # toast
    agreement_toastLocator = (By.XPATH, "//*[contains(@text,'账号')]")
