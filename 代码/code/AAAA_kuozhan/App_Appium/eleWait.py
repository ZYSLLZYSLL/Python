#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 11:24
# @Author : ZY
# @File : eleWait.py
# @Project : Appium
"""
    元素等待 三种
        1，强制等待
            time
        2，隐形等待
            # 隐形等待 智能等待 一般不单独使用 每个操作大概分配几秒的样子
            driver.implicitly_wait(10)
        3，显性等待
        locator = (By.ID, "com.tal.kaoyan:id/mainactivity_button_calendar")
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(locator))
        # WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_calendar"))
        # bDriverWait(driver, 20).until(lambda x: x.find_element(*locator))

"""

from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.webdriver import WebDriver
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "4LWSPFMBPV85EMPR",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": "True"
}

# 向服务端发送连接信息
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

# 显性等待
locator = (By.ID, "com.tal.kaoyan:id/mainactivity_button_calendar")
WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(locator))
# WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_calendar"))

# WebDriverWait(driver, 20).until(lambda x: x.find_element(*locator))

# driver.tap([(540, 1749)], 100)
