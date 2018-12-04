# -*-coding:utf-8 -*-
# File :basicDemo.py
# Author:George
# Date : 2018/12/4
"""
    Selenium + WebDriver 基本
    注意驱动和浏览器版本的兼容性
    IE 浏览器安全设置 Internet选项中 四个选项全部勾选
"""
import time
from selenium import webdriver

# 加载驱动 driver对应 chromedriver.exe的文件位置
driver = r'E:\Installation_packages\Chrome_plugins\chromedriver.exe'

# selenium自带firefox驱动
# browser = webdriver.Firefox()

# 通过驱动构建操作浏览器对象  chrome driver
browser = webdriver.Chrome(driver)

# 要打开的url
URL = 'http://www.baidu.com'

# 执行打开操作
browser.get(URL)

# 休眠2秒
time.sleep(2)

# 根据元素id查找输入框
input = browser.find_element_by_id('kw')

# 根据xpath寻找
# inputG = browser.find_element_by_xpath('//*[@id="kw"]')

# 根据css选择器查找
# input = browser.find_element_by_css_selector("#kw")

# 输入字符
input.send_keys('美女')

# 休眠
time.sleep(2)

# 找到搜索按钮
buttonSubmit = browser.find_element_by_id('su')

# 模拟点击动作
buttonSubmit.click()

time.sleep(5)

# 后退
browser.back()
time.sleep(2)

# 前进
browser.forward()
time.sleep(2)

# 退出
browser.quit()
print(dir(browser))
