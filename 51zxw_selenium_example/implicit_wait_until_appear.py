# -*-coding:utf-8 -*-
# File :implicit_wait_until_appear.py
# Author:George
# Date : 2018/12/23
"""
    隐式等待 等待全局整个页面的加载
    抛出错误可以自定义
    通过隐式等待或者显式等待 我们可以依据一定的页面情况去做对应操作 而非一刀切的 sleep() 动作 让我们的自动化程序更加合理，智能
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep, ctime


def get_firefox():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def implicit_waitG(url, content):
    firefox = get_firefox()

    firefox.get(url)

    # 让浏览器隐式等待 5 s (implicitly 隐式地)
    firefox.implicitly_wait(5)
    try:
        print(ctime())
        firefox.find_element_by_css_selector("#kw").send_keys(content)
        firefox.find_element_by_css_selector("#su")
    except NoSuchElementException as e:
        print(e)
    finally:
        print(ctime())
        firefox.close()
        firefox.quit()


if __name__ == "__main__":
    url = r'https://www.baidu.com/'
    content = "Resistant"
    implicit_waitG(url, content)
