# -*-coding:utf-8 -*-
# File :regularDemo.py
# Author:George
# Date : 2018/12/4
"""
    正则匹配 regular express Practice
    RPC Remote Procedure Call : 远程过程调用 一般企业内部的使用协议
    help(obj/module) dir(obj) 查看模块或者对象的可操作方法
"""
"""
    ()      标记一个子表达式的开始和结束位置
    .       除了空格之外的任意字符
    
"""
import re

quote = 'Freedom just like a cup of weak faint, george like the nature, just like a child boy 1 piece of love all share with the world 100 point faith 1,2, "545",ds45'

# re模块常见函数
# -----------findall------------
# 取出所有数字 注意观察抠出数字后还剩下什么  每个位置都留下了一个坑由 ,代替
pattern = re.compile(r'\D+')
# 匹配特定的单词 前两种都可以
# vocabulary = re.compile(r'\blove\b')
vocabulary = re.compile(r'\b(love)\b')
vacabularyFound = vocabulary.findall(quote)
# print(vacabularyFound)
result = pattern.findall(quote)
str = ','
for item in result:
    str += item
split_str = str.split(',')
# print(split_str)
# 切掉字符串中的 ''
list = [item for item in split_str if item != '']
# print(list)
# 寻找敏感词语
keyword = re.compile(r'\b\w+ie\w+\b')
result_kw = keyword.findall(quote)
print(result_kw)

# 剔除关键字 abc 不匹配含有abc的所有字符串 todo
abcExp = re.compile(r'((?!abc)|abc).+$')
testStr = 'hello abcde jack ad nddjbcasd'
result = abcExp.findall(testStr)
print(result)

# 按照关键字查找 比如要查找 含有abc关键字的字符串
abcGet = re.compile(r'\b\w+abc\w+\b')

# 这样写要求abc必连同前面的不间断字符处于开头位置 所以匹配不到
# abcGet = re.compile(r'^\b\w+abc\w+\b')
# 这样写要求abc联通后面字符必须为不间断处于结尾位置  所以也匹配不到
# abcGet = re.compile(r'\b\w+abc\w+\b$')
teststr_1 = 'hello dabcdsd thanks '
result = abcGet.findall(teststr_1)
print(result)

# --------------match--------------
# 从开始匹配匹配
pattern = re.compile(r'\bFre.*\b')
result = pattern.match(quote)
# print(result)

# --------------find----------------
# 返回第一个匹配成功的字符串
name = re.compile(r'\b\w*jack\w*\b')
nameOrder = 'hello jacknice  how are you '
nameResult = name.search(nameOrder)            # <re.Match object; span=(6, 14), match='jacknice'>
print(nameResult)
print(nameResult.group())      # jacknice
print(nameResult.group(0))      # jacknice
print('---------*----------')

# --------------group-----------------
numWord = '123hello4865'
pattern = re.compile(r'(\d+)(\w+)(\d+)')
result_v = pattern.search(numWord)
print('test usage of group')
print(result_v.group())
print(result_v.group(0))
print(result_v.group(1))    # 按照样式中括号提取 地区提第一个括号内容
print(result_v.group(2))    # 按照样式中括号提取 地区提第二个括号内容
print(result_v.group(3))    # 按照样式中括号提取 地区提第三个括号内容
print(result_v.groups())    # 返回元祖

# --------------sub-------------------
# re.sub(pattern, repl, string, count, flag)) 用于正则匹配要替换的字符串 默认全部替换
# 替换目标字符串 将目标中的ip地址替换成本地
url = 'https://113.215.20.136:9011/113.215.6.77/128.0.1.5c3pr90ntcya0/youku/6981496DC9913B8321BFE4A4E73/0300010E0C51F10D86F80703BAF2B1ADC67C80-E0F6-4FF8-B570-7DC5603F9F40.flv'
ip_v4 = re.compile(r'(25[0-5]|2[0-4][0-9]|[0-9]{0,1}[0-9][0-9]+.){3}(25[0-5]|2[0-4][0-9]|[0-9]{0,1}[0-9][0-9]+)')

# 这个能够将所有的ip匹配出来  magic
pattern = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
out = re.sub(pattern, '127.0.0.1', url)
print(out)
print(type(out))  # <class 'str'>

# --------------subs------------------
# re.subn(pattern, repl, string[, count])
str = 'today is a fine day work hard.com'
pattern = re.compile(r'\bwork\b')
out = re.subn(pattern, 'life', str)
print(out)
print(type(out))  # <class 'tuple'>  ('today is a fine day life hard.com', 1)
