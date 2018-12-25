# -*-coding:utf-8 -*-
# File :get_authInfo.py
# Author:George
# Date : 2018/12/6
"""
    通常我们用得最多的几种验证信息就是title、URL、text
    text 用于获取标签对之间的文本信息

"""
import time

from selenium import webdriver


def get_chrome():
    chrome = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    return chrome


def compare():
    chrome = get_chrome()

    url = 'https://www.oschina.net/home/login'

    # 打开对应页面资源
    chrome.get(url)

    time.sleep(5)
    print('-------------before login--------------')
    # 获取当前的title
    title = chrome.title  # 登录 - 开源中国社区

    # 获取当前页面的url
    current_url = chrome.current_url  # https://www.oschina.net/home/login
    print(f'before login the url is {current_url} and the title is {title}')

    # 执行登陆操作
    chrome.find_element_by_xpath(r"//div[@class='form-item']/div[@class='form-ctrl']/input[@id='userMail']").send_keys(
        '13554518280')

    chrome.find_element_by_xpath(
        r"//div[@class='form-item']/div[@class='form-ctrl']/input[@id='userPassword']").send_keys('kaige1992!!')

    # 点击登陆按钮
    chrome.find_element_by_xpath(r"//div[@class='login-form form-wrapper']/div/button").click()

    print('-------------------after login ------------------')
    time.sleep(5)
    title_after = chrome.title  # 开源中国 - 找到您想要的开源项目，分享和交流
    current_url_after = chrome.current_url  # https://www.oschina.net/?nocache=1544096303144

    print(f'now the title is {title_after}, the url is {current_url_after}')

    time.sleep(8)
    chrome.quit()


"""
    登陆前登陆后的url肯定会发生变化 按照url和title的变化 可以知道用户是否登陆成功 
    AS: 在登陆进账户后 记得休眠一段时间  就可以记录下来 url 发生的变化  可以在断言中进行比较判断
    
"""
