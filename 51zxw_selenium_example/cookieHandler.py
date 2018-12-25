# -*-coding:utf-8 -*-
# File :cookieHandler.py
# Author:George
# Date : 2018/12/25
"""
    在验证浏览器中cookie是否正确时，有时基于真实cookie的测试是无法通过白盒和集成测试进行的。Webdriver提供了操作Cookie的相关方法，可以读取，添加和删除cookie信息。
    常见 webdriver的cookie操作
    get_cookie(): 获取所有的cookie信息
    get_cookie(name): 返回字典的 key 为 name 的cookie
    add_cookie(cookie_dict): 添加cookie，"cookie_dict"指字典对象，必须有name 和 value 值。
    delete_cookie(name, optionString): 删除cookie信息，"name"是指要删除的 cookie 信息的名称。"optionString" 是指cookie的选项，目前支持的选项包括"路径"，"域"
    delete_all_cookies(): 删除所有的 cookie 信息
"""