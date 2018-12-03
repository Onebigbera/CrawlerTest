# -*-coding:utf-8 -*-
# File :urlBasic_g.py
# Author:George
# Date : 2018/12/3
"""
    urllib库在针对小型小型爬虫来说很强大 环境自带的包
"""
import urllib.request
import urllib.parse

URL = 'http://baidu.com'

# 发送一个get请求
result = urllib.request.urlopen(url=URL)

# 查看返回结果的可以调用方法
print(dir(result))

# 状态码 status  | 200
print(result.status)

# 获取url  | http://baidu.com
print(result.geturl())

# 获取 responseheaders | 将返回的headers展示出来
print(result.getheaders())

# 打印结果  |  <http.client.HTTPResponse object at 0x00000252DCACD828>   返回一个客户端HTTPResponse对象
print(result)

# 打印其类型 | <class 'http.client.HTTPResponse'>
print(type(result))

# 得到具体可以浏览的内容  具体的html文本
"""
    <html>
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
</html>

"""
print(result.read().decode('utf-8'))

# 下载并存储  retrieve: 检索 获取 获得
urllib.request.urlretrieve(url=URL, filename=r'F:\Testing_Automation\UnittestProjects\UnittestBasic\urllibPackges\downloads\Baidu.html')

# 通过url(uniform resource locator:统一资源定位符 ) 通过URI应用此方法可以获取该资源
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534153996436&di=924f4697b8fb3898310d4cfa3fc1759b&imgtype=0&src=http%3A%2F%2Fpic23.photophoto.cn%2F20120419%2F0033033921468983_b.jpg'

# 获取url对应的资源img | 也可以下载视频资源
urllib.request.urlretrieve(url=url, filename=r'F:\Testing_Automation\UnittestProjects\UnittestBasic\urllibPackges\downloads\stam.png')

# url中get方法传参数 带中文编码 不同字符集合时必须用quote url编码
strEncode = urllib.parse.quote("https://www.baidu.com/s?ie=utf-8&wd=中国")
# https%3A//www.baidu.com/s%3Fie%3Dutf-8%26wd%3D%E4%B8%AD%E5%9B%BD
print(strEncode)

# 将get参数进行解码  URL解码
strDecode = urllib.parse.unquote('https%3A//www.baidu.com/s%3Fie%3Dutf-8%26wd%3D%E4%B8%AD%E5%9B%BD')
# https://www.baidu.com/s?ie=utf-8&wd=中国
print(strDecode)
