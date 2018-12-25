# -*-coding:utf-8 -*-
# File :upload_fileG.py
# Author:George
# Date : 2018/12/24
"""
    文件上传也是 UI 测试中常见的一个操作，也是计算器基本功能之一
    webdriver 没有提供对应的方法，但是上传文件的条件都具备
    定位上上传文件按钮，通过send_keys 添加本地文件路径就可以了
"""

from webdriver_G import get_firefox, get_chrome
from time import sleep
import os


def uploadFileG():
    driver = get_chrome()
    file_path = r'F:\Testing_Development\UnittestProjects\UnittestBasic\51zxw_selenium_example\HTML_exmaplesG\uploadFile.html'
    driver.get(file_path)

    sleep(2)
    driver.close()

    # 定位到上传按钮 添加本地文件(路径)
    driver.find_element_by_name("file").send_keys(r"F:\test.txt")
    sleep(3)
    driver.close()
    driver.quit()


# 模拟向百度上传图片进行搜索
def uploadImageG(url, path):
    driver = get_firefox()
    driver.get(url)
    driver.find_element_by_css_selector(".soutu-btn").click()
    sleep(3)
    driver.find_element_by_css_selector(".upload-pic").send_keys(path)
    sleep(5)
    driver.close()
    driver.quit()

# 熟悉工具 Autoit

if __name__ == "__main__":
    # uploadFileG()
    # print(os.path.abspath("uploadFile.html"))
    url = r"https://www.baidu.com/"
    path = r"F:\Personal_Folder\Imagies\test1.jpg"
    uploadImageG(url, path)
