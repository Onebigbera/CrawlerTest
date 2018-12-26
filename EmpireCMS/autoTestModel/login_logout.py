# -*-coding:utf-8 -*-
# File :login_logout.py
# Author:George
# Date : 2018/12/26
"""
    线性模型模拟 : 模拟进行用户登入、登出操作
"""
from selenium import webdriver
from time import sleep


def get_driver():
    return webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')


def loginG(url=None):
    driver = get_driver()
    driver.get(url)
    sleep(2)

    # 先将可能存在的数据清除
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("george")
    driver.find_element_by_name("password").send_keys("kaige1992")
    driver.find_element_by_css_selector(".inputSub").click()
    sleep(3)
    return driver


def logout(url):
    driver = loginG(url)
    sleep(5)
    driver.find_element_by_xpath("//a[contains(text(),'退出')]").click()

    # 此时弹出退出弹框
    driver.switch_to_alert().accept()

    sleep(2)
    driver.close()
    driver.quit()


def main(url):
    logout(url)


if __name__ == "__main__":
    url = r'http://localhost/'
    main(url)
