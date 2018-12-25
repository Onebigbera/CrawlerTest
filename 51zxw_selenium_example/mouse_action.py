# -*-coding:utf-8 -*-
# File :mouse_action.py
# Author:George
# Date : 2018/12/23
"""
    鼠标操作是操作网页最常见的操作之一，常见的鼠标操作可以分类为:
    单击/双击/悬停/右击
与鼠标操作相关的模块: ActionChains

"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def get_firefox():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def test_mouse_actionG(url, content=None):
    firefox = get_firefox()
    firefox.get(url)

    # 设置为全屏
    firefox.maximize_window()
    sleep(1)

    # 定位到输入框并输入
    firefox.find_element_by_css_selector("#kw").send_keys("Selenium")

    # 定位到输入框  返回元素对象
    element = firefox.find_element_by_css_selector("#kw")
    # 双击操作 todo [george]  operation invalide
    ActionChains(firefox).double_click(element).perform()
    sleep(2)

    # 右击操作
    ActionChains(firefox).context_click(element).perform()


    # 鼠标悬停操作
    above = firefox.find_element_by_css_selector("[name='tj_settingicon']")
    ActionChains(firefox).move_to_element(above).perform()
    sleep(3)


    firefox.close()
    firefox.quit()

if __name__ == "__main__":
    url = r'https://www.baidu.com/'
    test_mouse_actionG(url)

