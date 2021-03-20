#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 9:12
# @Author : ZY
# @File : 01_denglu.py
# @Project : Appium

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.youkagames.gameplatform",
    "appActivity": "com.youkagames.gameplatform.activity.SplashActivity",
    "noReset": "False"
}

# desired_capabilities = {
#     "platformName": "Android",
#     "platformVersion": "10",
#     "deviceName": "4LWSPFMBPV85EMPR",
#     "appPackage": "com.youkagames.gameplatform",
#     "appActivity": "com.youkagames.gameplatform.activity.SplashActivity",
#     "noReset": "False"
# }

# 向服务端发送连接信息
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

driver.implicitly_wait(10)
locator = (By.ID, "com.youkagames.gameplatform:id/iv_cha")
WebDriverWait(driver, 10).until(lambda x: x.find_element(*locator))

driver.find_element_by_id("com.youkagames.gameplatform:id/iv_cha").click()  # 关闭新人福利
driver.find_element_by_id("com.youkagames.gameplatform:id/tv_positive").click()  # 同意协议
# driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()  # 允许电话权限 手机
# driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()  # 允许存储权限
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()  # 允许电话权限 模拟器
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()  # 允许存储权限
driver.find_element_by_xpath("//*[contains(@text,'我的')]").click()  # 点击我的
driver.find_element_by_id("com.youkagames.gameplatform:id/tv_name").click()  # 点击立即登录
driver.find_element_by_id("com.youkagames.gameplatform:id/phoneNum").send_keys("15239938038")  # 输入账号
driver.find_element_by_id("com.youkagames.gameplatform:id/password").send_keys("bowen123456")  # 输入密码
driver.find_element_by_id("com.youkagames.gameplatform:id/login").click()  # 点击登录
