# -*-coding:utf-8 -*-
# File :requestDemo.py
# Author:George
# Date : 2018/12/4
"""
    除了urllib库之外 request库也是一个不错的小型爬虫的库
    应用BS4 库进行爬虫分析
"""
from bs4 import BeautifulSoup as BS4
import requests

g_set = set()


# 定义存储文件的方法
def store_file(file_name, r):
    html_doc = r.text
    with open("geyan_%s.html" % file_name, 'w', encoding='utf-8') as fw:
        fw.write(html_doc)


# 定义下载文件的函数
def download_file(url, filename='index'):
    """

    :param url: 待下载页面地址
    :param filename:
    :return: 页面内容
    """
    # requests库请求url 获取文件
    r = requests.get(url)

    # 存储文件
    store_file(filename, r)
    return r

def parse_tbox(tbox, base_domain):
    """
    解析某个小说类别
    :param tbox:
    :param base_domain:
    :return:
    """
    tbox_tag = tbox.select("dt a")[0].text
    print(tbox_tag)

    index = 0
    li_list = tbox.find_all("li")
    for li in li_list:
        link = base_domain + li.a['href']
        print("index:%s, link:%s" % (index, link))
        index += 1
        if link not in g_set:
            g_set.add(link)
            filename = "%s_%s" % (tbox_tag, index)
            sub_html = download_file(link, filename)

def parse(response):
    """

    :param response: 对页面进行解析
    :return:
    """
    base_domin = response.url[:-1]
    g_set.add(base_domin)
    # print(base_domin)
    html_doc = response.content
    soup = BS4(html_doc, "lxml")
    tbox_list = soup.select("#p_left   dl.tbox")  # 小说
    [parse_tbox(tbox, base_domin) for tbox in tbox_list]

def main():
    base_url = "https://www.geyanw.com/"
    response = download_file(base_url)
    parse(response)

