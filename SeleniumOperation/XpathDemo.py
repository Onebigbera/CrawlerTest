# -*-coding:utf-8 -*-
# File :XpathDemo.py
# Author:George
# Date : 2018/12/4
"""
    使用Xpath 需要用到解析html解析库lxml
    需要熟悉Xpath基本使用语法
    从lxml导入etree会报红 & 输入下没有xpath方法 不要紧张
    当我们不确定结果是否正确 不能判断进行下一步操作时 直接将当前的对象dir(obj)自省一下
    批量获取 方便将数据对象中的多个属性批量获取
"""
import os

from lxml import etree

html_doc = None

# 文档来源我们可以自己简单实用urllib库进行获取
with open(r'F:\Testing_Automation\UnittestProjects\UnittestBasic\SeleniumOperation\TestDemo\Demo.html', 'r',
          encoding='utf-8') as f:
    html_doc = f.read()


# print(html_doc)

def etree_read(path):
    # etree
    etree_html = etree.parse(path)

    return etree_html


# 返回解析出来的parse对象
path = os.path.join('TestDemo', 'Demo.html')
# 返回parse解析树
etree_html = etree_read(path)
# 返回对象为列表 取某个文本
hehe_context = etree_html.xpath('//ol/li[@class="haha"]/text()')
print(type(hehe_context))  # <class 'list'>
print(hehe_context)

# 返回某个链接的用法 如何差异化寻找 如果要寻找上一个的url 也可以使用上一级差异对比  标签/@+属性 代表获取其属性
leijun_href = etree_html.xpath("//div[@id='pp']/div[@class='hh']/a/@href")
print(leijun_href)

# 批量获取 这里同时取了一个文本和一个 class  ['君不见黄河之水天上来，奔流到海不复回', 'hehe']
libai_id = etree_html.xpath("//div[@id='pp']/ol/li[@class='huanghe']/text()|//div[@id='pp']/ol/li[@id='tata']/@class ")
print(libai_id)
