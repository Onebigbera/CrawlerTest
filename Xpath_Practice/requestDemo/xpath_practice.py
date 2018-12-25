# -*-coding:utf-8 -*-
# File :xpath_practice.py
# Author:George
# Date : 2018/12/5
"""
    /   从根节点选择 元素的绝对位置
    //  不考虑节点的位置 匹配当前节点的文档的节点
    .   当前节点
    ..  当前节点的父节点
    @   选择属性
    bookstore  选取bookstore元素所有的子节点
    bookstore/book  选取属于bookstore子元素下的所有book元素
    // book 选取所有的book的子元素而不用管他们在文档中的位置
    bookstore//book 选取属于bookstore元素的后代book元素 而不管它处于bookstore节点的什么位置
    //@lang  选取名称为lang的所有属性


"""

