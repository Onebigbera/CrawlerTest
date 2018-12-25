# -*-coding:utf-8 -*-
# File :mouse_usage.py
# Author:George
# Date : 2018/12/6
"""
    鼠标模拟人进行点击、操作
    .click()


"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')


# 代开baidu页面
chrome.get('http://www.baidu.com')

#---------------ActionChains模块提供的常用操作方法------
#---------------悬停操作------------------
"""
    move_to_element()
"""
# 定位设置按钮上
# css_selector()  样式为:  #u1 > a.pf  id属性值为u1的下面的拥有class属性为pf的a标签
# settingButton = chrome.find_element_by_css_selector('#u1>a.pf').click()

# 模拟人进行悬停动作 记得传递
# ActionChains(chrome).move_to_element(settingButton).perform()

#-------------------右键点击事件-----------
"""
    context_click()
"""
# 找到百度一下按钮 右键点击
su = chrome.find_element_by_id('su')
# 鼠标右键点击事件
ActionChains(chrome).context_click(su).perform()
time.sleep(5)
#-----------------------------------------

#----------------双击--------------------
"""
    double_click()
"""
# 未测试
double_click_btn = chrome.find_element_by_xpath(r'xxx')
ActionChains(chrome).double_click(double_click_btn).perform()
#----------------拖动 鼠标推方操作--------------------
"""
    drag_and_drop()
    source:鼠标拖动的源元素
    target:鼠标释放的目标元素
    
"""
# eg:
# 定位到目标的源位置
source = chrome.find_element_by_xpath(r'xxx')

# 定位到元素要移动的目标位置
target = chrome.find_element_by_xpath(r'xxx')

# 执行元素的托放操作
ActionChains(chrome).drag_and_drop(source, target).perform()
#------------------------------------

chrome.quit()