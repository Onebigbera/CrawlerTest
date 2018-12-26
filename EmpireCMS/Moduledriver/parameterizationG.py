# -*-coding:utf-8 -*-
# File :parameterizationG.py
# Author:George
# Date : 2018/12/26
"""
    模型驱动测试将测试中各个功能单独分开，实现功能解耦，代码复用性；
    数据驱动测试就是将测试中固定数据进行参数化，实参转形参，方便模拟多组数据进行测试。
"""
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class Action(object):

    def loginG(self, driver, username, password, url):
        """

        :param driver: webdriver userd
        :param username: login name required
        :param password:  auth password
        :param url: login url
        :return:
        """
        driver.get(url)
        loginButton = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.NAME, 'username')))
        # 清掉可能出现在 input 框里面的残余信息
        loginButton.clear()
        loginButton.send_keys(username)
        driver.implicitly_wait(1.5)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_css_selector(".inputSub").click()
        driver.implicitly_wait(1)

    def logoutG(self, driver):
        """
        此时应该用户是登陆状态的 写一个类似与 login_requied() 语法糖 装饰器
        :param driver:
        :return:
        """
        # 只有登陆状态才会显示 “退出” 按钮
        exitButton = WebDriverWait(driver, 7, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, '退出')))
        driver.implicitly_wait(2)
        exitButton.click()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.delete_all_cookies()
        driver.close()
        driver.quit()


if __name__ == "__main__":
    UserDict = {
        'george': "kaige1992",
        'tom': "kaige1992",
    }
    url = r'http://localhost/'
    driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    for key, value in UserDict.items():
        Action().loginG(driver, key, value, url)
        Action().logoutG(driver)
        sleep(random.randrange(3, 5, 1))
