# -*-coding:utf-8 -*-
# File :auto_login.py
# Author:George
# Date : 2018/12/5
"""
    selenium 模块控制驱动模拟登陆 oschina
"""
from selenium import webdriver
import time


# 登陆操作 需要发送账号密码
def oschina_login():
    driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    url = "http://www.oschina.net/home/login"

    # 驱动获取url 模拟打开页面
    driver.get(url)

    # 模拟输入账户
    driver.find_element_by_id('userMail').send_keys('13554518280')

    time.sleep(2)
    # 模拟输入密码
    driver.find_element_by_id('userPassword').send_keys('kaige1992!!')

    time.sleep(2)

    driver.find_element_by_xpath("//*[contains(@class, 'btn btn-green block btn-login')]").click()
    time.sleep(3)
    return True

if __name__ =="__main__":
    oschina_login()