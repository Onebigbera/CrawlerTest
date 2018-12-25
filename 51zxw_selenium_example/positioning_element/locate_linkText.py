# -*-coding:utf-8 -*-
# File :locate_linkText.py
# Author:George
# Date : 2018/12/23
"""
    linkText DOM 对象中超链接文本  对 a 标签的操作

    get_element_by_link_text(): 输入完整的超链接文本 进行匹配
    get_element_by_partial_text() : 模糊搜索
    输入能够标识该超链接的局部文本来定位超链接文本
"""
from selenium import webdriver
from time import sleep


def get_firefox():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def locate_linktext(url):
    firefox = get_firefox()
    firefox.get(url)
    sleep(3)
    firefox.find_element_by_link_text("1-3 揭开自动化测试神秘面纱").click()
    sleep(3)

    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'http://www.51zxw.net/list.aspx?cid=615'
    locate_linktext(url)
