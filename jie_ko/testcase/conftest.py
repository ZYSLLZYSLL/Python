#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/20 16:13
# @Author : ZY
# @File : conftest.py
# @Project : jie_ko

import pytest
import json
import requests
from data.yamlData import readYaml
from common.basePage import LogHandler
from common.basePage import jiami

logger = LogHandler.logger


# 接口自动化
@pytest.fixture(params=readYaml("../data/key_chars_dict.yaml", "key", "chars"))
def z_m(request):
    logger.info(f"当前测试的是key={request.param[0]}，chars={request.param[1]}")
    # print(f"\n当前测试的是key={request.param[0]}，chars={request.param[1]}")
    url = "http://v.juhe.cn/cccn/to_telecodes.php"
    para = f"key={request.param[0]}&chars={request.param[1]}"  # 参数
    # get请求时，参数要传给params
    res = requests.get(url, params=para)
    return res, request.param[0], request.param[1]


@pytest.fixture(params=readYaml("../data/m_z.yaml", "key", "telecodes"))
def m_z(request):
    logger.info(f"当前测试的是key={request.param[0]}，chars={request.param[1]}")
    url = "http://v.juhe.cn/cccn/to_chinese.php"
    head = {"Content-Type": "multipart/form-data"}
    # head = {"Content-Type": "multipart/json"}

    para = f"key={request.param[0]}&telecodes={request.param[1]}"

    # para = json.dumps(para).encode("utf-8")
    res = requests.post(url, headers=head, params=para)
    return res, request.param[0], request.param[1]


def bai():
    url = "http://192.168.10.44:6088"
    # post请求时，带上content-type字段,头部字段传给headers
    head = {"Content-Type": "application/json"}  # 头部字段
    para = {"name": "博文", "no": jiami(201102)}
    # 把pare数据格式变成json格式
    para = json.dumps(para).encode("utf-8")
    # post请求时，参数要传给data
    res = requests.post(url, headers=head, data=para)
    print(res)
    print(type(res))
    return res
