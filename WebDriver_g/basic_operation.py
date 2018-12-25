# -*-coding:utf-8 -*-
# File :basic_operation.py
# Author:George
# Date : 2018/12/5
"""
    after we find the object what we do next is important the basic operation in selenium is the
    obj.clear()  clear the text if the object is a  textbox at present
    obj.send_keys() simulate our hand put word in the textbox
    obj.click()  simulate our hand to click the button or submit key  各种框框、链接可以点击的元素都可以进行点击
    obj.submit() 也是提交作用在某些时候二者作用一样
"""
import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')


def basic():
    url = 'http://www.baidu.com'

    chrome.get(url)
    chrome.find_element_by_xpath("//form/span/input[@id='kw']").send_keys('美女')

    time.sleep(3)
    # 清除输入框内容
    chrome.find_element_by_xpath("//form/span/input[@id='kw']").clear()

    # 重新输入  连续输入可以进行输入拼接
    chrome.find_element_by_xpath("//form/span/input[@id='kw']").send_keys('数学建模')

    chrome.find_element_by_xpath("//input[@value='百度一下']").click()

    time.sleep(3)
    chrome.quit()


def login_163(url):
    chrome.get(url)

    time.sleep(2)

    chrome.find_element_by_id("auto-id-1544013009850").send_keys('onebigbera')

    chrome.find_element_by_id('auto-id-1544013009853').send_keys('kaige1992!!')

    time.sleep(1)
    chrome.find_element_by_link_text("登陆").click()

    time.sleep(3)
    chrome.quit()
url = 'https://mail.163.com/'
login_163(url)