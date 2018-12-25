# -*-coding:utf-8 -*-
# File :multiwindows_operate.py
# Author:George
# Date : 2018/12/24

from time import sleep
from webdriver_G import get_firefox

"""
    场景需求:
        打开特定网站，获取页面的标题和url, 点击某个链接，获取页面的url和标题，再关闭该页面，返回到之前页面，关闭浏览器退出
"""


def multiWindowsOperate(url, content=None):
    # 获取浏览器驱动
    driver = get_firefox()

    # 代开对应页面
    driver.get(url)
    sleep(2)
    url_title = driver.title
    # 获取窗口当前句柄
    window_handle = driver.current_window_handle
    print(f"当前获取到的页面句柄为{window_handle}, 标题为 {url_title}")
    sleep(2)

    # 通过部分链接文字定位并点击某个链接后 跳转到其他页面
    driver.find_element_by_partial_link_text("2-6").click()
    sleep(5)

    # 只是浏览器隐式等待5s
    # driver.implicitly_wait(5)

    # 切换为特定句柄页面
    driver.switch_to.window(window_handle)

    # 点击另外一个链接
    driver.find_element_by_partial_link_text('2-5').click()
    sleep(10)

    # get the title

    # 获取全部的 handle
    # handles = driver.window_handles
    # print(type(handles))

    # 按照列表的操作方法进行操作切换handle 切换到最后一个 handle
    # driver.switch_to.window(handles[-1])

    # 关闭当前窗口
    driver.close()
    sleep(2)
    # 关闭全部窗口 退出浏览器
    driver.quit()


if __name__ == "__main__":
    url = r'http://www.51zxw.net/list.aspx?cid=615'
    multiWindowsOperate(url)
