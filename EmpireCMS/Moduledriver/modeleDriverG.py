# -*-coding:utf-8 -*-
# File :modeleDriverG.py
# Author:George
# Date : 2018/12/26
"""
    为了增加代码的复用性和可维护性，将测试用例中的功能进行封装，以便提高程序的简洁性、可读性和优雅
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os


class George(object):

    def __init__(self, driver_path, **kwargs):
        """

        :param url: 要访问的 url
        :param driver_path: 驱动的路径
        :param kwargs: 驱动相关的关键字参数
        """
        self.driver = webdriver.Chrome(executable_path=driver_path, **kwargs)

    def login(self, url):
        self.driver.get(url=url)
        loginButton = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.NAME, 'username')))
        loginButton.clear()
        loginButton.send_keys("george")
        self.driver.find_element_by_name("password").send_keys("kaige1992")
        self.driver.find_element_by_css_selector(".inputSub").click()
        time.sleep(3)
        return self.driver

    def screenShot(self, url):
        """
        这里截图的前提是用户已经登陆
        :param url: 访问的 url
        :param screen_dir: 照片存储目录
        :return:
        """
        screen_dir = 'F:\\Testing_Development\\UnittestProjects\\UnittestBasic\\EmpireCMS\\screenShot'
        try:
            if not os.path.exists(screen_dir):
                os.mkdir(screen_dir)
                print(f"{screen_dir} 目录创建成功！")
            else:
                print("目录已经存在")
        except BaseException as msg:
            print(msg)

        driver = self.login(url)
        time.sleep(4)
        picture_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        try:
            # 将场景记录下来
            status = driver.save_screenshot(screen_dir + "\\" + picture_time + ".png")
            print(f"截图状态为{status}")
        except BaseException as msg:
            print(msg)
        return driver

    def logout(self):
        """
        这里应该加一个判断，判断用户是否处于登陆状态，只有在登陆后才会退出登陆
        :return:
        """
        self.driver.find_element_by_xpath("//a[contains(text(),'退出')]").click()

        self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    driver_path = r'E:\Installation_packages\Chrome_plugins\chromedriver.exe'
    url = r'http://localhost/'
    Vuser = George(driver_path)
    # Vuser.login(url)
    Vuser.screenShot(url)
    Vuser.logout()