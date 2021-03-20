#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 10:03
# @Author : ZY
# @File : 01_connectApp.py
# @Project : Appium

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


"""
    元素查找+元素操作（4大操作）
    元素查找：
        id
        accessbilityid
        class
        uiaumator
        xpath
        name
    元素操作：
        click（点击） 
        input（输入） 
        swipe（滑动） 
        text（获取文本）
"""
# 元素定位操作
driver.find_element_by_id("com.tal.kaoyan:id/tip_commit").click()  # 通过id找到元素，然后点击
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/view_wemedia_cacel").click()  # 通过id找到元素，然后点击
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/kaoyan_home_schtip_close").click()  # 通过id找到元素，然后点击
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()  # 通过id找到元素，然后点击
# list(driver.find_elements_by_class_name("android.widget.RadioButton"))[3].click()  # 通过class找到元素，然后点击
time.sleep(3)

driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()  # 点击未登录，进入大老爷们儿
time.sleep(3)


driver.find_element_by_id("com.tal.kaoyan:id/login_code_touname").click()  # 点击密码登录
time.sleep(3)
# driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").click()  # 点击输入账号框
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("15239938038")  # 输入账号
time.sleep(3)
# driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").click()  # 点击输入密码框
# time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("bowen123456")  # 输入密码
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_treaty_checkbox_password").click()  # 勾选同意协议
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()  # 点击登录
time.sleep(3)

