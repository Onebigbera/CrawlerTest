# -*-coding:utf-8 -*-
# File :popUp_AlertHandler.py
# Author:George
# Date : 2018/12/24
"""
    弹窗是浏览器操作方式中常见的操作 使用脚本处理窗口模拟人为操作
"""

from time import sleep
from webdriver_G import get_chrome


def popUp_AlertG(url):
    firefox = get_chrome()
    firefox.get(url)

    # 点击设置按钮
    firefox.find_element_by_link_text("设置").click()
    sleep(2)

    # 点击选项
    firefox.find_element_by_link_text("搜索设置").click()
    sleep(3)

    # 点击保存设置选项
    firefox.find_element_by_link_text("保存设置").click()
    sleep(1)

    # 点击后跳出弹窗按钮 切换到弹窗对象上
    pop_window = firefox.switch_to_alert()
    pop_window.accept()
    sleep(3)

    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r"https://www.baidu.com/"
    popUp_AlertG(url)
