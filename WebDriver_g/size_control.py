# -*-coding:utf-8 -*-
# File :web_control.py
# Author:George
# Date : 2018/12/4
"""
    了解定位元素后(xpath css 正则)等  下一步就要控制我们的浏览器 首先改变它的大小哦
"""
from selenium import webdriver
import time

# 生成驱动
driver = r'E:\Installation_packages\Chrome_plugins\chromedriver.exe'

# 生成浏览器模拟对象
chrome = webdriver.Chrome(driver)

# 操作的URL
URL = 'http://www.baidu.com'

# 将浏览器设置为全屏
# chrome.maximize_window()

# 单位为像素
# chrome.set_window_size(1200, 1200)
chrome.get(URL)

# 获取某个标签的大小
size = chrome.find_element_by_id('kw').size
print(size)     # {'height': 22, 'width': 500}
time.sleep(3)

# 获取某个元素的某个属性   get_attribute  获取输入框的type属性
attr = chrome.find_element_by_id('kw').get_attribute('type')
print(attr)      # text 即输入框的type属性值为text 文本

# 获取某个输入框文本的text值
"""
    非常有用的方法 在做断言时通过选择的时做比较
"""
# chrome.find_element_by_id('kw').send_keys('hello world')
# time.sleep(3)
# text = chrome.find_element_by_id('kw').text
time.sleep(3)

# 将整个p标签 <p><a>text</text>...</p>内容都返回过来
text_o = chrome.find_element_by_id('cp').text
print(text_o)
# print(text)

# is_display 显示元素是否显示出来 返回boolean
for i in range(10):
    if chrome.find_element_by_id('kw').is_displayed():
        print(True)
        break
    else:
        time.sleep(1)
        print('---waiting---')



# 全拼显示
# chrome.maximize_window()
"""
    chrome.get("http://m.mail.10086.cn")
    # 参数数字为像素点
    chrome.set_window_size(480,800)
    chrome.quit()
    应用场景: 用移动端来测试时  就需要重新指定宽、高
"""
chrome.quit()
