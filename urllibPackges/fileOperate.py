# -*-coding:utf-8 -*-
# File :fileOperate.py
# Author:George
# Date : 2018/12/3
"""
    url的魔法 其实url中压根就没有那么复杂
    思考: URL中那么长的链子到底是啥呢？？？？
    经过在百度上搜索美女 如果是自动搜索会出现很长的url = https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3&rsv_spt=1&rsv_iqid=0xc1628ff300008ae7&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=7&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=1772&rsv_sug4=2403&rsv_sug=1
    但是当我们将浏览器上可以看到的美女后面删除后结果是一样的
    得出结论: 后面带的信息对我们要搜索的内容不产生影响
    URL 编码/解码网站 http://tool.chinaz.com/tools/urlencode.aspx

    针对get请求的转码
    quote: 对字符串进行编码
    unquote: 对字符串进行解码

"""
import urllib.parse
import urllib.request

keyWord = input('请输入你要查询的词语:')

# 因为输入中带有中文 需要将keyWord编码
encodedKeyWord = urllib.parse.quote(keyWord)

# url 拼接 将含有中文字符的参数进行编码后再拼接
URL = "http://www.baidu.com/s?ie=utf-8&wd=" + encodedKeyWord

# 自己构建一个headers
headers = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)'
}

# --------------方法一---------------------
# 构造一个请求对象
# request = urllib.request.Request(url=URL, headers=headers)
# -----------------------------------------


# ----------------方法二-------------------
# 自己构建一个请求
request = urllib.request.Request(url=URL)

# 伪造UA 添加UA
request.add_header("User-Agent", 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)')
# ------------------------------------------

# 发送请求 返回结果
result = urllib.request.urlopen(request)

# 将返回的界面存储到设定文件夹中  'wb' 二进制写入是不会有编码冲突的
# with open(r'F:\Testing_Automation\UnittestProjects\UnittestBasic\urllibPackges\downloads\girls.html', 'wb') as fw:
#     fw.write(result.read())

# 方法二 : 按照特定的编码方式写入(utf-8)
with open(r'F:\Testing_Automation\UnittestProjects\UnittestBasic\urllibPackges\downloads\girls.html', 'w',
          encoding='utf-8') as fw:
    # 注意utf-8写入 将内容读取read后也要utf-8解码
    fw.write(result.read().decode('utf-8'))
