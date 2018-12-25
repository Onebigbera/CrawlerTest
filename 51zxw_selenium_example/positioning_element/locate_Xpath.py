# -*-coding:utf-8 -*-
# File :locate_Xpath.py
# Author:George
# Date : 2018/12/23
"""
    使用 Xpath XML 路径语言定位，功能强大
    /  "使用绝对定位 从根节点开始寻找"
    // "使用相对定位"  根据属性和逻辑判断定位元素
"""
from selenium import webdriver
from time import sleep


def get_firefox():
    firefox = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')
    return firefox


def Xpath_locateG(url, content=None):
    firefox = get_firefox()
    firefox.get(url)

    # 记住 : 由 try path 提供的路径有可能只是一个值 而我们需要找到那个可以点击的链接  这里是纯按照标签的数学逻辑结构寻找的
    print(firefox.current_url)
    firefox.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/ul[2]/li[46]").click()
    sleep(3)
    print(firefox.current_url)
    firefox.find_element_by_xpath('//div[@class="defail-buy"]/a[@id="defailBuy"]').click()
    sleep(3)
    print(firefox.title)
    firefox.close()
    firefox.quit()



def logic_Xpath(url, content=None):
    firefox = get_firefox()
    firefox.get(url)
    firefox.find_element_by_xpath("//input[@id='loginStr' and @placeholder='用户名/邮箱/手机号']").send_keys('13554518280')
    sleep(2)
    firefox.find_element_by_xpath("//input[@id='pwd']").send_keys('kaige1992!!')
    sleep(2)
    firefox.find_element_by_xpath("//button[@type='submit']").click()
    sleep(5)
    firefox.close()
    firefox.quit()


if __name__ == "__main__":
    url = r'https://lol.qq.com/data/info-heros.shtml'
    # Xpath_locateG(url)
    url1 = r'http://www.51zxw.net/login'
    logic_Xpath(url1)