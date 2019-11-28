#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from selenium import webdriver
# 导入time模块在进行测试时每一步暂停1s,对抗反爬虫
import time
from urllib import request
import os  # 对文件夹操作的模块


# 构造函数
def Getphoto(name):
    # 准备一个网址
    url = 'http://movie.douban.com/'
    # 打开谷歌浏览器
    browser = webdriver.Chrome(executable_path='E:/chromedriver_win32/chromedriver.exe')
    # 进入豆瓣
    browser.get(url)

    # 1.找到输入并框输入姓名自动搜索
    time.sleep(1)
    shuru = browser.find_element_by_id('inp-query')
    time.sleep(1)
    shuru.send_keys(name)
    time.sleep(1)
    button = browser.find_elements_by_class_name('inp-btn')[0].find_elements_by_tag_name('input')[0]
    time.sleep(1)
    button.click()
    # 2.寻找搜索结果的人物链接
    detail = browser.find_elements_by_class_name('detail')[0]
    href = detail.find_elements_by_class_name('title')[0].find_elements_by_tag_name('a')[0].get_attribute('href')
    # 3.拼接成实际需要的图片网址
    url = href + 'photos/'
    # 4.关闭浏览器得到网页编码
    browser.get(url)
    lis = browser.find_element_by_id('content').find_element_by_tag_name('ul').find_elements_by_tag_name('li')
    srcList = []
    # 迭代出所有的src并添加到列表srcList
    for each in lis:
        src = each.find_elements_by_tag_name('img')[0].get_attribute('src')
        print(src)
        srcList.append(src)
    print(srcList)
    # 创建一个文件夹，名称为name
    try:
        os.mkdir(name)
    except FileExistsError as e:
        print(e)
    # 进入这个文件夹
    os.chdir(name)
    # 迭代出所有图片
    for i, v in enumerate(srcList):
        request.urlretrieve(v, str(i + 1) + '.jpg')
    browser.close()


if __name__ == '__main__':
    # 实例化，输入你想爬取的名字
    Getphoto('刘亦菲')
    # browser = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
    # # 进入豆瓣
    # browser.get("http://www.baidu.com")
    # print(browser.page_source)
    # browser.close()
