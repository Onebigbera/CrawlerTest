# -*-coding:utf-8 -*-
# File :scrollbarOperateG.py
# Author:George
# Date : 2018/12/25
"""
    操作滚动条是 UI 测试中常见的内容，某些网页内容必须得拉到下面才会慢慢加载出对应页面元素，比如淘宝、亚马逊等。
"""

from webdriver_G import get_firefox, get_chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random


def scrollbar_operate_basic(url):
    driver = get_firefox()
    driver.get(url)

    """
        滚动条并不再DOM中，所以我们得靠JS操作来控制页面滚动操作
    """

    # 定义要操作得js 行为 源生js语句

    """
        var action=documentElement.scrollTop=1000 是源生的js语句(类比于数据库中MySQL语句)
        scrollTop: 限定滚动条距离顶部的距离
    """
    js_action = "var action=document.documentElement.scrollTop=10000"
    driver.execute_script(js_action)

    time.sleep(3)
    # 设置 scrollTop=0 即为回到顶端
    js_action = "var action=document.documentElement.scrollTop=0"
    driver.execute_script(js_action)
    time.sleep(5)

    driver.close()
    driver.quit()


"""
    进入 Amazon 网站下拉到末尾 找到网站的下一页网站并点击
"""


def scrollbarOperateG(url):
    # 实例化一个 webdriver 的可选项对象
    chromeOption = webdriver.ChromeOptions()
    # xpath-helper 文件位置
    xpath_extension_path = r'E:\Installation_packages\Chrome_plugins\xpath-helper.crx'
    # 加载 xpath 插件、
    chromeOption.add_extension(xpath_extension_path)
    # 将加载了 xpath 的参数和chrome_driver 的路径都添加进去 创建driver 对象
    driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe',
                              options=chromeOption)
    driver.get(url)
    # random(start, end, step)
    time.sleep(random.randrange(5, 10, 1))
    # 找到 Next Page 按钮，属于可见元素
    # js 代码有两种写法 但是对元素要求不一样， focus更严格

    # 第一种 focus
    # targetEle = driver.find_element_by_css_selector("#pagnNextString")
    # driver.execute_script("arguments[0].focus();", targetEle)

    # 第二种写法  因为我们没有注册和填写相关信息 所以 Amazon 会弹出弹窗来干扰 我们影响执行 但是思路和代码没有问题
    targetEle = driver.find_element_by_xpath("//a[@id='pagnNextLink']/span[@id='pagnNextString']")
    driver.execute_script("arguments[0].scrollIntoView();", targetEle)

    # 第三种写法  通过 tab 定位到特殊按钮(准确的说是我们目标键的上一个 tab 位按钮)
    # 找到 Next Page 按钮 属于可见元素
    # 指定元素是超链接 —————— 可以用 tab 键切换到
    targetEle = driver.find_element_by_xpath("//a[@id='pagnNextLink']")

    # 这个元素是个 span 标签不是超链接 无法接收 tab 键
    # targeEle = driver.find_element_by_xpath("//a[@id='pageNextLink']/span[@id='pagnNextString']")
    targetEle.send_keys(Keys.TAB)
    print("结束拖动滚动条")

    time.sleep(5)
    driver.close()
    driver.quit()


if __name__ == "__main__":
    url = r'http://www.51zxw.net/list.aspx?page=3&cid=615'
    # scrollbar_operate_basic(url)
    Amazon = r'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=phone'
    scrollbarOperateG(Amazon)
