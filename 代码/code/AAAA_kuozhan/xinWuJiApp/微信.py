#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/4 15:02
# @Author : ZY
# @File : 微信.py
# @Project : code
import os
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "4LWSPFMBPV85EMPR",
    "appPackage": "com.tencent.mm",
    "appActivity": "com.tencent.mm.ui.LauncherUI",
    "noReset": "True"
}

command_executor = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(command_executor, desired_capabilities)
#
a = (By.ID, "com.tencent.mm:id/a2_")
WebDriverWait(driver, 20).until(lambda x: x.find_element(*a))
# driver.tap([(556, 451)], 0)
# time.sleep(3)
# driver.tap([(606, 1049)], 0)
# time.sleep(3)
driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout').click()
time.sleep(3)
driver.find_element_by_id("com.tencent.mm:id/ava").click()
time.sleep(3)
driver.find_element_by_id("com.tencent.mm:id/ay9").click()
time.sleep(3)
driver.tap([(360, 1483)], 0)
time.sleep(3)
b = 1
while True:
    driver.tap([(340, 1783)], 0)
    time.sleep(0.01)
    print(f"发送了{b}次")
    b += 1

# driver.implicitly_wait(10)
# time.sleep(5)
# driver.find_element_by_id('com.vivo.gamecube:id/btn_sure')  # 确认游戏助手
# driver.find_element_by_id('com.vivo.gamecube:id/btn_sure')  # 确认游戏助手
# driver.find_element_by_id('com.vivo.gamecube:id/btn_sure')  # 确认游戏助手

# driver.implicitly_wait(10)
# driver.find_element_by_id('com.tencent.mm:id/dtx').click()  # 点击通讯录
# driver.tap([(398, 2322)], 100)
# os.popen('adb shell input tap 398 2322')
