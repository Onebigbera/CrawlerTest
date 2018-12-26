# -*-coding:utf-8 -*-
# File :teacherDemo.py
# Author:George
# Date : 2018/12/26
"""
    定义一个用户的类，实现用户登陆和登出的方法
"""
from selenium import webdriver
from time import sleep


class Login(object):

    def loginG(self, driver, url):
        driver.get(url)
        driver.implicitly_wait(5)
        driver.find_element_by_name("username").clear()
        sleep(1)
        driver.find_element_by_name("username").send_keys("george")
        sleep(1)
        driver.find_element_by_name("password").send_keys("kaige1992")
        driver.find_element_by_css_selector(".inputSub").click()
        driver.implicitly_wait(2)

    def logoutG(self, driver):
        driver.find_element_by_xpath("//a[contains(text(),'退出')]").click()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(1)
        driver.close()
        driver.quit()


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    url = r'http://localhost/'
    Login().loginG(driver, url)
    sleep(3)
    # 这是的 driver 是哪一个呢？
    Login().logoutG(driver)
