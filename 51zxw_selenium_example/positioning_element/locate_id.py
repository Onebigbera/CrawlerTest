# -*-coding:utf-8 -*-
# File :locate_id.py
# Author:George
# Date : 2018/12/23
"""
    打开百度浏览器 输入搜索内容 点击搜索按钮
"""
from selenium import webdriver
from time import sleep


def get_firefox_driverG():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


# 打开网页并搜索
def search_actionG(url, content):
    firefox = get_firefox_driverG()

    firefox.get(url)
    sleep(3)

    # 操控元素的第一步是定位元素,然后再向输入框输入内容
    # firefox.find_element_by_id("kw").send_keys(content)
    firefox.find_element_by_name('wd').send_keys(content)
    # 定位到搜索点击按钮
    firefox.find_element_by_id('su').click()
    sleep(3)

    print(firefox.title)             # 打印当前页面标题
    print(firefox.current_url)       # 打印当前页面url
    sleep(3)
    firefox.close()


if __name__ == "__main__":
    url = 'https://www.baidu.com/'
    content = "武汉大学"
    search_actionG(url, content)
