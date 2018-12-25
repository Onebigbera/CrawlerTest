# -*-coding:utf-8 -*-
# File :wait_untilAppearG.py
# Author:George
# Date : 2018/12/23
"""
    由于网络延迟和服务器响应的滞后性，页面并不能总是第一时间刷新，因此就需要等待页面刷新判定成功后再操作。
    相关模块
    WebDiverWait  显式等待必用 明显某个元素没出现 显式的
    NoSuchElementException 用于隐式等待异常抛出

    expected_conditions 与其条件类(包含方法可以调用，用于显式等待)
    By 用于元素定位

"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep

"""
    explicit waiting  显式等待
    implicit waiting  隐式等待
"""


def get_firefox():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


# 显式等待直到某个元素出现
def check_actionG(url, content):
    firefox = get_firefox()

    firefox.get(url)
    firefox.find_element_by_css_selector("#kw").send_keys(content)

    # 请记住 这个函数有返回值 返回的就是等待的元素
    element = WebDriverWait(firefox,5, 0.5).until(EC.presence_of_element_located((By.ID,'su')))
    element.click()

    sleep(3)
    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'https://www.baidu.com/'
    content = 'Selenium'

    check_actionG(url, content)