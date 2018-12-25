# -*-coding:utf-8 -*-
# File :loading_file_waitting.py
# Author:George
# Date : 2018/12/6
"""
    如今大多数的 web 应用程序使用 AJAX 技术。当浏览器在加载页面时，页面内的元素可能并不是同时
被 加 载 完 成 的 ， 这 给 元 素 的 定 位 添 加 的 困 难  如 果 因 为 在 加 载 某 个 元 素 时 延 迟 而 造 成
ElementNotVisibleException 的情况出现，那么就会降低的自动化脚本的稳定性
    WebDriver 提供了两种类型的等待：显式等待和隐式等待
"""
import time

"""
    显式等待:WebDriver等待某个条件成立时继续执行否则在达到最长时抛出超时异常(TimeOutException) WebDriverWait
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_chrome():
    chrome = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    return chrome


def wait_loading():
    chrome = get_chrome()
    chrome.get("http://www.baidu.com")

    # 设置等待的方法
    # element = WebDriverWait(chrome, 5, 0.5).until(EC.presence_of_element_located((By.ID,"kw")))

    """
        WebDriverWait() 是由webdriver提供的等待方法。在设置时间内，默认每隔一段时间就会检测一次(poll_frequency)当前页面元素是否存在。如果超过设置监视检测不到就会抛出异常，具体格式如下：
        WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
        参数说明:
        diver: webdriver的驱动(Ie|Firefox|Chrome)
        timeout: 最长超时时间，默认单位为秒
        poll_frequency : 休眠时间的间隔(步长)时间，默认为0.5秒
        ignored_exceptions: 超时后的异常信息，默认情况下抛出NoSuchElementException异常
        until() : webdriver 一般由until(或者until_not)方法配合使用，线面是util()和until_not()的用法
        
        until(method, message="")
        调用该方法提供的驱动程序作为一个参数，直到返回值为True
        
        until_not(method, message="")
        调用改方法提供的驱动程序作为一个参数，直到返回值为False
        
        
    Expected Conditions
        本例中，我们在使用expected_conditons类时对其进行了重命名，通过as关键字将其重命名为EC,并且调用presence_of_element_located()判断元素是否存在
        expected_conditions 类提供了一些预期条件的实现
        title_is                            用于判断标题是否为xx
        title_contatin                      用于判断标题是否包含
        presece_of_element_located          用于判断元素是否存在
        visibility_of_element_located       判断元素是否可见
        vivibility_of                       是否可见
        presence_of_all_elements_located    判断一组元素是否存在
        text_to_be_present_in_element       判断元素是否有xx文本信息
        text_to_be_present_in_element_value 判断元素值是否有xx文本信息
        frame_to_be_avaliable_and_switch_to_it 表单是否可用 并且切换到它
        invisibility_of_element_located      判断元素是否隐藏
        element_to_be_clickable              判断元素是否点击，它处于可见和启动状态
        staleness                           判断元素不再时依附于DOM
        element_to_be_selected              被选中的元素
        element_located_to_be_selected      一个期望的元素位于被选中
        element_selection_state_to_be       一个期望检查如果给定的元素被选中
        element_located_state_to_be          期望找到一个元素并检查是否选择状态       
        alert_is_present                    预期一个警告信息
        除了expected_conditons所提供的方法外，我们也可以使用is_displayed()来判断元素是否可用
        
    """
    # 方法二 实现判断id为kw的输入框是否可用
    # -----------start---------------------
    input_ = chrome.find_element_by_id("kw")

    # 结合lambda 函数 返回引擎  只有元素展示了 引擎才能继续工作 todo what is the element then???
    element = WebDriverWait(chrome, 5, 0.5).until(lambda chrome: input_.is_displayed())

    input_.send_keys('hello world')
    # ---------------end-------------------

    # element.send_keys('selenium')
    time.sleep(3)

    chrome.quit()
