#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/1 20:13
# @Author : ZY
# @File : a.py
# @Project : app_xingneng

# 新建a.txt并写入内容
# f = open('a.txt', 'w', encoding='utf-8')
# f.write('1\na,b,c,d\n123,4,5,6\n中,国,富,强,123')
# f.close()


# 新建a.txt并写入内容
# f = open('a.txt', 'r', encoding='utf-8')
# f1 = open('a.csv', 'w', encoding='ANSI')
# f1.write(f.read())
# f.close()
# f1.close()

# f = open('a.txt', 'w', encoding='utf-8')
# f1 = open('a.csv', 'r', encoding='ANSI')
# f.write(f1.read())
# f1.close()
# f.close()


class ExcelMutualTxt:

    def run(self):
        self.show_menu()
        while True:
            menu_num = int(input('请输入您需要的功能序号:'))

            if menu_num == 1:
                self.e_zhaun_t()
            elif menu_num == 2:
                self.t_zhaun_e()
            elif menu_num == 3:
                break

    @staticmethod
    def show_menu():
        print('请选择如下功能——————————————————————')
        print('1:Excel转Txt')
        print('2:Txt转Excel')
        print('3:退出系统')

    def e_zhaun_t(self):
        f = open('a.txt', 'w', encoding='utf-8')
        f1 = open('a.csv', 'r', encoding='ANSI')
        f.write(f1.read())
        f1.close()
        f.close()
        print('Excel转TxT转换完成')

    def t_zhaun_e(self):
        f = open('a.txt', 'r', encoding='utf-8')
        f1 = open('a.csv', 'w', encoding='ANSI')
        f1.write(f.read())
        f.close()
        f1.close()
        print('TxT转Excel转换完成')


aa = ExcelMutualTxt()
aa.run()
