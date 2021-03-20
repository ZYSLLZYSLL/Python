#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 16:12
# @Author : ZY
# @File : 04_高级手势操作.py
# @Project : Appium

# 连接app  参数  http协议
from appium import webdriver  # 模块
from appium.webdriver.common.touch_action import TouchAction
import time

# 构造参数
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.ChooseLockPattern",
    "noReset": "False"
}

# 向服务端发送连接信息
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
'''
 action = TouchAction(self)

 action \
        # 用手按住
        .press(x=start_x, y=start_y) \
        # 等待ms
        .wait(ms=duration) \
        # 移动到哪个地方
        .move_to(x=end_x, y=end_y) \
        # 手松开
        .release()
 # 执行操作           
 action.perform()
'''
# 可以拐弯的手势
TouchAction(driver).press(None, 800, 487).move_to(None, 800, 730).move_to(None, 925, 730).release().perform()
