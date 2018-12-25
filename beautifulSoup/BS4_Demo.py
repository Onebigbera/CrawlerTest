# -*-coding:utf-8 -*-
# File :BS4_Demo.py
# Author:George
# Date : 2018/12/5
"""
    BeautifulSoup 一种基于CSS选择器来进行元素定位的文本解析工具解析库 css选择器  CssStyle-Selector
    Beautiful Soup 自动将文本转化为二进制Unicode编码 基于CSS导航查找
    Beautiful Soup 可以跳跃式取值
    Xpath  文本节点选取 转化为树行文本  DocNodes-Selector 基于XML层次节点定位
    re    正则 文本属性匹配选择

选择器种类
    类选择器   <div class="xxx">
    id选择器   <div id='xxx'>   Beautiful Soup 就是一个ID选择器  css样式
    标签选择器  <div></div> div 本身就是一个标签
    获取对象后 对于url的操作 一般要去掉最后的'/' 取得最后的域名
"""
from bs4 import BeautifulSoup as BSP4
import requests


def downLoad(url):
    result = requests.get(url)

    # <Response [200]>
    # print(result)

    # http://www.geyan123.com/
    # print(result.url)

    # http://www.geyan123.com
    # print(result.url[:-1])

    # 响应对象的content 内容我们需要的进行解析的对象 得到Html文本对象
    html_doc = result.content
    print(html_doc)

    # 将文本存储到本地
    # with open(r'F:\Testing_Automation\UnittestProjects\UnittestBasic\beautifulSoup\HtmlDoc\geyan.html', 'w') as fw:
    #     fw.write(html_doc.decode('gbk'))

    # 返回一个文本响应对象
    # return result
    return result

    #


def parse(response):
    """

    :param response: 通过requests.get(url)方法得到的response对象
    :return:
    """
    # 获取域名
    domain = response.url[:-1]

    # 得到html文本
    html_doc = response.content

    # 使用Beautiful Soup 解析文本 生成soup对象
    soup = BSP4(html_doc, "lxml")

    # 可以看到很多的soup对象的操作方法
    # print(dir(soup))

    # 按照box 进行解析出来todo 分析页面 其每一个专栏部分都是安排在一个tbox中间  所有tbox在上一级别种
    # todo 寻找id为 p_left的标签下面的所有的 class为tbox的标签 所以p_left前面需要加#  p_left 是个id的标签值
    tbox_list = soup.select("#p_left .tbox")

    print(type(tbox_list))  # <class 'list'>
    # 遍历tbox列表  进行相关操作
    for tbox in tbox_list:
        parse_tbox(tbox)


# 定义解析tbox的函数
def parse_tbox(tbox):
    """

    :param tbox: 得到页面class为tbox中的单个tbox选项 每个节点  BS4选择器是可以跳跃性的  可以不按照顺序取值
    :return:
    """
    # 找到tbox下面的所有的li
    li_list = tbox.find_all('li')
    for li in li_list:
        a_href = li.a["href"]
        # 取到我们第二层抓取的入口  /renshenggeyan/31110.html 直接将原页面和这个页面拼接就可以
        print(a_href)
        title = li.a["title"]
        print(title)

    return  True


def main():
    return


if __name__ == "__main__":
    url = 'http://www.geyan123.com/'
    response = downLoad(url)
    parse(response)
