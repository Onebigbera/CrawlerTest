# -*-coding:utf-8 -*-
# File :callLoginMethond.py
# Author:George
# Date : 2018/12/26
"""
    从外部导入模块 直接调用类中的方法 当不能导入我们自定义的模块时，可以将我们定义模块的文件夹右键选择 Make Directory as Source Root
    当我们定义更多方法 都可以在此处进行几种管理，在登陆和登出之间进行操作
"""
from teacherDemo import Login
from selenium import webdriver


def simulateOperate(driver, url):
    Login().loginG(driver, url)
    driver.implicitly_wait(5)
    Login().logoutG(driver)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    url = r'http://localhost/'
    simulateOperate(driver, url)
