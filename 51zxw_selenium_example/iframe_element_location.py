# -*-coding:utf-8 -*-
# File :iframe_element_location.py
# Author:George
# Date : 2018/12/24

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

# 自己定义的工具类
from webdriver_G import get_firefox, get_chrome

"""
    从自己写的接口引入类或者函数时，路径(相对路径/绝对路径一定要正确)
"""
""""""


def iframe_element_locate(url, content=None):
    firefox = get_chrome()
    # 打开本地 iframe 文本
    firefox.get(url)

    """
        重要的一点 切换到 frame 页面
        search : frame 内嵌样式的 sogou 搜索页面的 "id"
    """
    firefox.switch_to.frame("search")
    firefox.find_element_by_css_selector("#query").send_keys('frame')
    element = WebDriverWait(firefox, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'stb')))
    element.click()

    sleep(3)
    # 设置显式等待
    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'F:\Testing_Development\UnittestProjects\UnittestBasic\51zxw_selenium_example\HTML_exmaplesG\frame_example.html'
    iframe_element_locate(url)
