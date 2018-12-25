# -*-coding:utf-8 -*-
# File :logAnalyze.py
# Author:George
# Date : 2018/12/5
"""
    日志分析是程序员生活中重要的一部分 如何有效的提取出日志中的有效内容 并且优美的展示呢？
    已知日志固定格式，现在要将日志内容结合文字展示出来
"""
import os
import re


def logHandler(filePath):
    """

    :param filePath:
    :return:
    """
    # 编码/解码问题 具体问题具体分析
    with open(filePath, 'r',encoding='utf-16') as fr:
        try:
            logLines = fr.readlines()
            num = 0
            for log in logLines:
                print(log)
                print(type(log))
                event = re.compile(r'[0-9]{12}')
                managerId = re.compile(r'[0-9]{0,3}$')
                event_obj = event.search(log)
                manager_obj = managerId.search(log)
                num +=1
                # 用group方法 将日志中的具体内容取出来
                print(f'The event is {event_obj.group()}, manager_obj is {manager_obj.group()}')
            print(f'Total hava {num} logOperations')
        except Exception as e:
            print(e)

def findLogInfo():
        """

        :param path: 存放日志文件的位置
        此处不带入日志文件 已知单行日志信息为:
        log_str = "[DEBUG][2018-08-10 09:10:34][192.168.12.16]"
        :return:
        """

        log = "[DEBUG][2018-09-12 12:21:25][192.168.52.14][function1]"
        # 首先日志以[]分隔 每个[]包括单元都是一个整体 []使用转义
        """
            一 按照[]切分 []要匹配  匹配时用 '\'转义
            二 大写P<参数>形式匹配 记得加括号 因为参数和匹配对象为整体
            三 匹配多次
        """
        regStr =re.compile(r"\[(?P<log_levlel>.*?)\]\[(?P<log_time>.*?)\]\[(?P<ip_addr>.*)?\]\[(?P<log_foo>.*?)\]")

        # 两种方式编译都可以 加了() 会将每个匹配的部分变为自动整个串的 字串
        info = re.compile(r"\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]")
        result_G = info.findall(log)
        result = regStr.findall(log)
        print('--------log----------')
        print(result_G)
        # 元祖对应赋值
        (log_info, log_time, log_IP, log_foo) = result_G[0]
        str = f'the level is {log_info}, and the time is {log_time}, ip is {log_IP}, function is {log_foo}'
        print(str)

        print(result)
        return str

if __name__ == '__main__':
    logHandler(r'F:\Testing_Automation\UnittestProjects\UnittestBasic\Xpath_Practice\requestDemo\events.log')
    findLogInfo()