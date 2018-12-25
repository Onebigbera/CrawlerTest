# -*-coding:utf-8 -*-
# File :pull_down_list_operatG.py
# Author:George
# Date : 2018/12/23
"""
    首先得熟悉下拉菜单的页面代码结构:
    <select class='xx' name='CookieData'>
        <option value='1'>留一天'</option>
        <option value='2'>留三天'</option>
        <option value='3'>留七天'</option>
    </select>
    每个标签都有其 value 值 每个标签成对出现
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select


def get_firefoxG():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def choice_pullListG(url, content=None):
    firefox = get_firefoxG()
    firefox.get(url)
    sleep(2)

    # 选择下拉菜单下拉框方法一 :  click 点击选定
    # 根据标签名称 'option' 获取所有标签集合 按照索引取得操作对象 用 click 点击选定操作
    firefox.find_elements_by_tag_name('option')[0].click()

    # 通过value 来定位 css定位
    firefox.find_element_by_css_selector("[value='2']").click()
    sleep(3)


    # 选定 下拉菜单框方法二
    """
        步骤分解:
        1. 先定位到 select 元素标签
        2. 元素标签通过索引选择对应可选项
        
    """
    select = Select(firefox.find_element_by_css_selector("[name='CookieData']"))
    """
        选取 select 标签下面选项的三种方法
    """
    # 根据所用选择
    select.select_by_index(1)
    # 根据文本值选择
    select.select_by_visible_text('留一年')
    # 根据 option 标签的属性 value 值 来定位
    select.select_by_value('3')


    firefox.close()
    firefox.quit()






