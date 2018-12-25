# -*-coding:utf-8 -*-
# File :getScreenShotG.py
# Author:George
# Date : 2018/12/25
"""
    屏幕截图是一个常见的记录问题的方法，通过截图可以留下依据供我们进行分析
    通过 webdriver 自带的截图函数 只需要将截图的名称和存储位置进行设置即可
"""

from webdriver_G import get_chrome
import time
import os


def getScreenShotG(url):
    """

    :param url: 要访问的url
    :return:
    """
    driver = get_chrome()
    driver.get(url)
    time.sleep(3)
    # 注意时间的转换
    picture_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    try:
        # 返回的是 True 路径拼接
        picture_status = driver.get_screenshot_as_file(
            'F:\\Testing_Development\\UnittestProjects\\UnittestBasic\\51zxw_selenium_example\\HTML_exmaplesG\\' + picture_time + '.png')
        print(f'{picture_status} 截图成功')
    except BaseException as msg:
        print(msg)
        time.sleep(2)
        driver.close()
        driver.quit()


# 使用 save_screenshot() 函数
def saveScreenShot(url):
    # 记录下照片的生成时间
    picture = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))

    # 创建保存照片的目录
    picture_directory = 'F:\\Testing_Development\\UnittestProjects\\UnittestBasic\\51zxw_selenium_example\\HTML_exmaplesG'

    # 打印工作目录
    print(os.getcwd())

    try:
        # 如果目录改位后面带了"\\"不会报错但是执行异常
        if not os.path.exists(picture_directory):
            os.mkdir(picture_directory)
            print(f"{picture_directory} 目录创建成功")
        else:
            print("目录已经存在")
    except BaseException as msg:
        print(msg)

    driver = get_chrome()
    driver.get(url)
    time.sleep(5)

    try:

        status = driver.save_screenshot(picture_directory + "\\" + picture + ".png")
        print(f"{status} 截图完成")
    except BaseException as msg:
        print(msg)
    driver.close()
    driver.quit()


if __name__ == "__main__":
    url = r"http://img.zcool.cn/community/0317abd579af1af0000012e7eb711e3.jpg"
    # getScreenShotG(url)
    saveScreenShot(url)
