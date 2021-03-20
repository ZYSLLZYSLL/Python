#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 17:23
# @Author : ZY
# @File : 06_多点触控.py
# @Project : Appium

from appium.webdriver.common.multi_action import MultiAction

# 连接app  参数  http协议
from appium import webdriver  # 模块
from appium.webdriver.common.touch_action import TouchAction
import time

# 构造参数
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.baidu.BaiduMap",
    "appActivity": "com.baidu.baidumaps.MapsActivity",
    "noReset": "True"
}
# 向服务端发送连接信息
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
time.sleep(10)
action1 = TouchAction(driver)
action1.press(None, 388, 394).move_to(None, 548, 207).wait(200).release()
action2 = TouchAction(driver)
action2.press(None, 388, 394).move_to(None, 548, 207).wait(200).release()
mu1 = MultiAction(driver)
mu1.add(action1, action2)
mu1.perform()

# os.popen('adb shell input tap 971 2300')  # 根据坐标点击屏幕

# driver.tap([(540, 1749)], 100)


