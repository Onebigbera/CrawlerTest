# -*-coding:utf-8 -*-
# File :foward_back.py
# Author:George
# Date : 2018/12/4
"""
    模拟浏览器进行前进和后退页面   该操作是具有上下文语义 context
    测试阶段如果遭到浏览器拦截 开启ip 代理和 UA 代理

"""
import time

from WebDriver_g.size_control import chrome
from selenium import webdriver


def add_agency():

    chromeOptions = webdriver.ChromeOptions()
    # 设置ip代理 一定要注意 两边都不能有空格
    chromeOptions.add_argument("--proxy-server=http://ip:port")
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get("http://httpbin.org/ip")
    time.sleep(4)
    browser.quit()

# forward_back
def forward_back_g(driver):
    """

    :param driver: chrome driver
    :return:
    """
    # 访问百度首页
    URL = 'http://baidu.com'
    driver.get(URL)

    time.sleep(2)

    # 跳转到新闻页面
    # 根据link的 text内容寻找 "新闻是一个超链接的文本"
    driver.find_element_by_link_text('新闻').click()
    # URL_V1 = 'http://news.baidu.com'
    # print(f'now access {URL_V1}')
    # driver.get(URL_V1)

    # 后退到首页
    print(f'back to {URL}')
    driver.back()

    time.sleep(3)
    # 前进到新闻页面
    # print(f'forward to {URL_V1}')

    # time.sleep(6)
    driver.forward()

    driver.quit()

if __name__ == "__main__":
    # forward_back_g(chrome)
    add_agency()