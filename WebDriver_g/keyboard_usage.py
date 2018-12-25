# -*-coding:utf-8 -*-
# File :keyboard_usage.py
# Author:George
# Date : 2018/12/6
"""
    与键盘相关的类 Keys  基本的键盘相关操作都能模拟出来
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


def get_chrome():
    chrome = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    return chrome


chrome = get_chrome()
chrome.get('http://www.baidu.com')
"""
    常见方法
"""
#--------------------------------------------------
# 向输入框输入内容
chrome.find_element_by_id('kw').send_keys('seleniumm')
time.sleep(2)

#-------------------------------------------------
# ctrl+a 将上一步多输入的内容清掉
chrome.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(2)

#------------------------------------------------
chrome.find_element_by_id('kw').send_keys('教程')
time.sleep(2)

#--------------------------------------------------
# ctrl+a 全选输入框内容
chrome.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
time.sleep(2)

#--------------------------------------------------
# ctrl+x 剪切输入框内容
chrome.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
time.sleep(2)

#---------------------------------------------------
# ctrl+v 将粘贴板中内容粘贴到输入输入框中
chrome.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
time.sleep(2)

#---------------------------------------------------
# 回车 通过回车来代替点击进行操作查询动作
chrome.find_element_by_id('kw').send_keys(Keys.ENTER)

time.sleep(3)

# 离开
chrome.quit()
