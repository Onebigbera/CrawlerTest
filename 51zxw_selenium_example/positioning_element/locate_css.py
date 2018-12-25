# -*-coding:utf-8 -*-
# File :locate_css.py
# Author:George
# Date : 2018/12/23
"""
    Selenium 中推荐 CSS 样式定位，其在查找元素中表现更快，语法也更简洁
    常见 CSS 定位用法:
    find_element_by_css_selector()
    #id id选择器 根据 id 属性来定位元素
    .class class 选择器 根据class属性来定位元素
    [attribute='value'] 更具属性值来定位元素
    element > element  根据元素层级来定位元素
"""
from selenium import webdriver
from time import sleep


def get_firefox():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def locate_cssG(url, content=None):
    firefox = get_firefox()
    firefox.get(url)

    # 记住 : 永远不要再一棵树上吊死 当没法通过 .class_value  来娶到  也可以用 #id_value 来取
    # 第一种 通过 class 属性定位
    firefox.find_element_by_css_selector(".s_ipt").send_keys("Selenium")
    sleep(3)

    # 第二种 通过 id  属性定位
    firefox.find_element_by_css_selector("#kw").send_keys("Hello world")
    # 清空输入信息
    firefox.find_element_by_css_selector("#kw").clear()
    sleep(3)

    # 第三种 通过属性定位 [attribute='value']
    firefox.find_element_by_css_selector("[autocomplete='off']").send_keys('there are many road yong man')
    sleep(3)

    # 第四种 按照结构层级来定位 比如 定位到密码输入框就加个 [type='password']等
    firefox.find_element_by_css_selector("form#form>span>input[name='wd']").send_keys('Selenium is amazing')
    sleep(3)

    firefox.find_element_by_css_selector("#su").click()
    sleep(2)

    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'https://www.baidu.com/'
    locate_cssG(url)
