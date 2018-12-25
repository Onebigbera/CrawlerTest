# -*-coding:utf-8 -*-
# File :loading_file_waitting_implied.py
# Author:George
# Date : 2018/12/6
"""
    隐式等待
    隐式等待是通过一定的市场来等待页面所有元素加载完成。如果超出了设置的超时时间还未加载就抛出NoSuchElementException异常
    webdriver提供了implicitly_wait()方法来实现隐式等待，默认设置为零，它的用法相对简单
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_chrome():
    chrome = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    return chrome

def wait_implicitly_g():
    chrome = get_chrome()
    url = 'http://baidu.com'

    # 不做判断先等待10s
    chrome.implicitly_wait(10)

    chrome.get(url)
    input = chrome.find_element_by_id("kw")
    # 首先会不断轮询 判断是否定位到了id为kwss的元素
    # input = chrome.find_element_by_id("kwss")
    input.send_keys('selenium is funny')
    time.sleep(3)
    chrome.quit()

wait_implicitly_g()
"""
    implicitly_wait()默认参数的单位为秒  本例中设置等待时长为 10 秒 首先这 10 秒并非一个固定的等 待时间，它并不影响脚本的执行速度
    其次，它并不真对页面上的某一元素进行等待，当脚本执行到某个元素定位时，如果元素可定位那么继续执行，如果元素定位不到，那么它将以轮询的方式不断的判断元素
是否被定位到，假设在第 6 秒钟定位到元素则继续执行 。直接超出设置时长（10 秒）还没定位到元素则抛出异常


"""