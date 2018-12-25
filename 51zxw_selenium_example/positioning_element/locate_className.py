# -*-coding:utf-8 -*-
# File :locate_className.py
# Author:George
# Date : 2018/12/23
"""
    className 是 DOM 中唯一标识符，所以使用 className 时会获取拥有相同类名的元素集合
"""
from selenium import webdriver
from time import sleep


def get_firefoxG():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


# 通过className 定位
def locate_className(url, content):
    firefox = get_firefoxG()

    firefox.get(url)

    firefox.find_element_by_class_name('search-input').send_keys(content)
    sleep(3)
    firefox.find_element_by_class_name('search_btn').click()
    sleep(3)

    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'http://www.51zxw.net/'
    content = 'Selenium'
    locate_className(url, content)
