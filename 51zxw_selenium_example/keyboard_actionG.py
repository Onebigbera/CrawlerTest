# -*-coding:utf-8 -*-
# File :keyboard_actionG.py
# Author:George
# Date : 2018/12/23
"""
    模拟常见的键盘操作
    需要用到的模块 Keys
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def get_firefox():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def keyBoard_actionG(url, url1=None):
    firefox = get_firefox()
    firefox.get(url)

    # 定位到输入框并输入内容
    firefox.find_element_by_css_selector("#kw").send_keys('Python')

    # 定位到输入框并且全选输入框内容  相当于通过键盘 向输入框输入 ctrl + a 操作
    firefox.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, 'a')
    sleep(1)

    # 定位到输入框将全选的框内内容进行复制或者剪切
    firefox.find_element_by_css_selector("[id='kw']").send_keys(Keys.CONTROL, 'c')
    sleep(1)

    # 剪切操作
    # firefox.find_element_by_css_selector("[id='kw']").send_keys(Keys.CONTROL, 'x')

    # 打开 Bing 浏览器
    firefox.get(url1)

    # 将粘贴板上内容复制到 Bing 浏览器输入框内
    firefox.find_element_by_css_selector("#query").send_keys(Keys.CONTROL, 'v')
    sleep(2)

    # 点击搜索按钮进行搜索
    firefox.find_element_by_id('stb').click()
    sleep(5)

    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'https://www.baidu.com/'
    url1 = r'http://sogou.com/'
    keyBoard_actionG(url, url1)
