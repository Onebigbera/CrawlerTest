# -*-coding:utf-8 -*-
# File :drive_your_browser.py
# Author:George
# Date : 2018/12/23
"""
    使用 FireFox 来进行 Selenium 相关操作
    注意 : 当在一次操作中打印多个 url 时候 就会覆盖前面
"""

from selenium import webdriver
from time import sleep


# 定义获取 geckodriver 的驱动对象
def get_firefox_driverG():
    driver = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return driver


# 定义打开关闭浏览器的操作
def open_browser(url, url1):
    driver = get_firefox_driverG()
    driver.get(url)
    # 打印打开设定网页的标题
    print(driver.title)
    sleep(3)
    driver.get(url1)
    sleep(3)
    driver.close()


if __name__ == "__main__":
    url = "https://www.baidu.com/"
    url1 = "http://www.51zxw.net/list.aspx?page=2&cid=615"
    open_browser(url, url1)