# -*-coding:utf-8 -*-
# File :webdriver_G.py
# Author:George
# Date : 2018/12/24
"""
    将自己经常用到的代码块进行总结归类是程序员的一个基本素养和习惯
    todo(george : to be optimized)
"""

from selenium import webdriver


# class WebDriverG(object):
#
#     def __init__(self, executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe'):
#         self.executable_path = executable_path
#
#
#     def get_firefox(self):
#         firefox = webdriver.Firefox(executable_path=self.executable_path)
#         return firefox

def get_firefox():
    return webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')


def get_chrome(**kwargs):
    return webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
