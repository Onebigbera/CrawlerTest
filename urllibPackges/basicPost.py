# -*-coding:utf-8 -*-
# File :basicPost.py
# Author:George
# Date : 2018/12/4

"""
    测试基本的post方法提交数据 需要提交数据的操作
    编码 转码操作
    字符串(str)====》字节(byte) encode编码(采取Unicode方式编码 使用双字节方式编码字符串)
    字节(byte)====》字符串(str) decode解码
    read()读取出来的是二进制数据(bit/byte) 转换成srt需要解码

    针对post方法的编码
    urllib.parse.urlencode(data).encode('utf-8')
"""
import json
import urllib.request
import urllib.parse

url = 'http://fanyi.baidu.com/sug'

# UA 是最基本的伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

word = input('请输入要查询的词语:')

# post中提交表单
data = {
    'kw': word
}

# 编码动作 按照utf-8编码 针对post请求参数的转码 编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 构建请求对象  自定义伪装请求
request = urllib.request.Request(url=url, headers=headers, data=data)

# 发送请求 urlopen() 参数里面可以放 url 可以放 request对象
result = urllib.request.urlopen(request)

# 读取查看 读取转码
resultDecoded = result.read().decode('utf-8')

# 将返回的json字符串转换成python对象(json字典对象)
jsonResult = json.loads(resultDecoded)

# 将python对象转换为json字符串 确保编码不出错
str = json.dumps(jsonResult, ensure_ascii=False)

with open(r'F:\Testing_Automation\UnittestProjects\UnittestBasic\urllibPackges\downloads\json.json', 'w', encoding='utf-8') as fw:
    fw.write(str)

