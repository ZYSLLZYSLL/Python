#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 15:31
# @Author : ZY
# @File : 03_swip.py
# @Project : Appium

""""
    滑动
"""

# 连接app  参数  http协议
from appium import webdriver  # 模块
import time

# 构造参数
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.HomeTabActivity",
    "noReset": "False"
}

# 向服务端发送连接信息
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

# 隐形等待 智能等待 一般不单独使用 每个操作大概分配几秒的样子
driver.implicitly_wait(10)

# 元素定位操作
driver.find_element_by_id("com.tal.kaoyan:id/tip_commit").click()  # 通过id找到元素，然后点击
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/view_wemedia_cacel").click()  # 通过id找到元素，然后点击
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/kaoyan_home_schtip_close").click()  # 通过id找到元素，然后点击
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()  # 通过id找到元素，然后点击
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()  # 点击未登录，进入大老爷们儿
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_code_touname").click()  # 点击密码登录
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("15239938038")  # 输入账号
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("bowen123456")  # 输入密码
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_treaty_checkbox_password").click()  # 勾选同意协议
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()  # 点击登录
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_forum").click()  # 点击社区

# 获取手机屏幕大小
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

driver.swipe(x * 0.3, y * 0.8, x * 0.3, y * 0.15, duration=10000)  # 向上滑动社区内容
# driver.swipe(300, 1100, 300, 300)  # 向上滑动社区内容
