# -*-coding:utf-8 -*-
# File :download_Files.py
# Author:George
# Date : 2018/12/24
"""
    文件下载是浏览器常见功能

"""
from selenium import webdriver
from time import sleep


def downLoadG(url):
    # 获取 firefox profile 文件对象
    profile = webdriver.FirefoxProfile()

    # 设置下载地址
    profile.set_preference("browser.download.dir", 'F:\Download_Files\Firefox_Download')

    # 设置下载到指定文件夹
    profile.set_preference("browser.download.folderList", 2)

    # 设置开始下载时 不提醒
    profile.set_preference('browser.download.manager.showWhenStarting', False)

    # 设置对于 zip 类型不用询问
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

    # 创建驱动对象 注意参数
    driver = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe',
                               firefox_profile=profile)

    driver.get(url)
    sleep(5)
    # 定位到下载的链接
    driver.find_element_by_xpath("/html/body/a[1]").click()

    sleep(20)

    driver.close()
    driver.quit()


if __name__ == "__main__":
    url = r'http://sahitest.com/demo/saveAs.htm'
    downLoadG(url)
