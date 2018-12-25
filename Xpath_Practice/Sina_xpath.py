# -*-coding:utf-8 -*-
# File :Sina_xpath.py
# Author:George
# Date : 2018/12/6
"""
    测试新浪网站 使用xpath提取网页信息
    取到的都是
"""
import time

from selenium import webdriver

chrome = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver')
# 检验路径是否拼写正确
# print(dir(chrome))

url = 'https://www.sina.com.cn/'

# 模拟打开 url 新浪网站| 也可以本地下载好HTML文件 再解析本地HTML
chrome.get(url)

# <selenium.webdriver.remote.webelement.WebElement (session="959ba5bd3a9e1b97a4cf6c15825a7811", element="0.17020209319376778-1")>
result = chrome.find_element_by_xpath(r"//div[@class='newslist']/div[@id='syncad_0'][1]")
href = chrome.find_element_by_xpath(r"//div[@id='fc_B_pic']/div/a/img/@src")
print(href)

print(result)
time.sleep(4)
chrome.quit()