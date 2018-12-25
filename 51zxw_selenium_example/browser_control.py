# -*-coding:utf-8 -*-
# File :browser_control.py
# Author:George
# Date : 2018/12/23
"""
    常见浏览器控制操作:
        设置浏览器窗口大小
        控制浏览器页面前进后退
        页面刷新
"""

from selenium import webdriver
from time import sleep


# get the driver
def get_firefox_driverG():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def operate_browserG(url, url1):
    firefox = get_firefox_driverG()
    firefox.get(url)

    # 设置窗口为最大化
    firefox.maximize_window()
    sleep(3)

    firefox.get(url1)
    # 设置特定大小的窗口
    firefox.set_window_size(400, 800)

    # 回退到上一个页面
    firefox.back()
    sleep(2)

    # 刷新浏览器
    firefox.refresh()
    sleep(3)
    firefox.close()


if __name__ == "__main__":
    url = "http://www.51zxw.net"
    url1 = "http://www.51zxw.net/show.aspx?id=60544&cid=615"
    operate_browserG(url, url1)
