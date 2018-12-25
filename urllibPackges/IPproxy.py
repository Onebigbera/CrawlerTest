# -*-coding:utf-8 -*-
# File :IPproxy.py
# Author:George
# Date : 2018/12/4

"""
    使用ip代理池 多进程爬取  使用队列方式进行进程间通讯
"""
import time
import requests

import threading
from threading import Lock
# 使用队列
import queue

# 实例化一个线程锁
g_lock = Lock()
# 开启的线程数目
n_thread = 10

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/68.0.3440.106 Safari/537.36",

}

