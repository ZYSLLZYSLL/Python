#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/9 11:09
# @Author : ZY
# @File : yaml_01.py
# @Project : code

import yaml

# with open("conf.yml", "r", encoding='utf-8') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     print(type(data))
#     print(data)

data = {
    "father": {'name': '张三', 'age': 18},
    'mother': {'name': '王云', 'age': 19}
}

with open("a.yml", 'w', encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True)
