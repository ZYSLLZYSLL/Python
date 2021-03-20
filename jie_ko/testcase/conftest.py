#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/20 16:13
# @Author : ZY
# @File : conftest.py
# @Project : jie_ko

import pytest
import requests


# 接口自动化
@pytest.fixture()
def biaozhendianma():
    url = "http://v.juhe.cn/cccn/to_telecodes.php"
    para = "key=229bb81cac0b96ed627afe1362b6ba2c&chars=周宇"  # 参数
    # res = requests.get(url, params=para).text
    # return res
    return url, para
