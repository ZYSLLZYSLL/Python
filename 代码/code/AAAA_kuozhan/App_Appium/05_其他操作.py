#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 17:06
# @Author : ZY
# @File : 05_其他操作.py
# @Project : Appium

from appium import webdriver  # 模块
from AAAA_kuozhan.log_ri_zhi.log_01 import Logg

a = Logg()

# 构造参数
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.HomeTabActivity",
    "noReset": "False"
}
# desired_capabilities = {
#     "platformName": "Android",
#     "platformVersion": "10",
#     "deviceName": "4LWSPFMBPV85EMPR",
#     "appPackage": "com.tal.kaoyan",
#     "appActivity": ".ui.activity.SplashActivity",
#     "noReset": "True"
#     # "app": r"E:\Python\Appium\App_Appium\百度地图.apk" # 安装app
# }

# 向服务端发送连接信息
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

# # 打开其他app
# driver.start_activity('com.tal.kaoyan', 'com.tal.kaoyan.ui.activity.HomeTabActivity')

# 安装app
# driver.install_app(r'E:\Python\Appium\App_Appium\百度地图.apk')  # 里面填写路径

# 卸载app
# driver.remove_app('包名')

# 判断app是否存在
# driver.is_app_installed('包名')

a.get_info('截图')
a.get_DEBUG('调试')

# 截图
# time.sleep(4)
driver.get_screenshot_as_file(r"E:\Python\Appium\aboutApp\a\a.png")
