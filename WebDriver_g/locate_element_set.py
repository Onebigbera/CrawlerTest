# -*-coding:utf-8 -*-
# File :locate_element_set.py
# Author:George
# Date : 2018/12/6

"""
    定位一组元素
    WebDriver 提供了以下的用于定义一组元素的8中定位方法
"""
"""
    find_elements_by_id()
    find_elements_by_name()
    find_elements_by_class_name()
    find_elements_by_class_name()
    find_elements_by_tag_name()
    find_elements_by_link_text()
    find_elements_by_partial_link_text()
    find_elements_by_xpath()
    find_elements_by_css_selector()
    定义一组对象的方法与定义单个对象的方法类似，唯一的区别就是在单词element变为了复数，定位一组数据一般用于以下场景:
    
    *批量操作对象，比如将页面上所有的复选框都勾选
    *选获取一组对象然后再这组对象中过滤中满足特定需求的对象。比如:在页面上的所有checkbox  然后选择最后一个
   
"""
from selenium import webdriver
import os
