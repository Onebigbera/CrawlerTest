# -*-coding:utf-8 -*-
# File :locate_tagname.py
# Author:George
# Date : 2018/12/23
"""
    通过 tag_name(标签名称)来获取DOM 对象，是获取到所有名为给定值的标签，默认为第一个
"""
from selenium import webdriver
from time import sleep


def get_firefox_driverG():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def locate_tagName(url, content):
    firefox = get_firefox_driverG()

    firefox.get(url)

    # 找到所有的标签名为 "input"的标签并输入值
    firefox.find_element_by_tag_name("input").send_keys(content)
    sleep(3)

    # 向指定找到的 input 标签中输入值
    # firefox.find_element_by_tag_name("input")[0].send_keys(content)
    # sleep(3)
    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'http://www.51zxw.net/'
    content = 'selenium'
    locate_tagName(url,content)

