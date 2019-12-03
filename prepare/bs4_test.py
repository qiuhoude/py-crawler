#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

"""
主要的类
Tag 每个标签都是一个Tag
BeautifulSoup 也是Tag的子类
NavigableString bs4中封装的string
Comment NavigableString的子类,获取html中的注释信息


"""


def getHtmlStr():
    with open("boss_golang.html", "r", encoding="utf-8") as fd:
        html = fd.read()
        return html


def tagElement():
    html = getHtmlStr()
    # 创建 Beautiful Soup 对象
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    # print(soup.head)

    # 它查找的是在所有内容中的第一个符合要求的标签 ,第一个a标签
    print(type(soup.a))
    # 第一个p标签
    print(soup.p)

    # [document] #soup 对象本身比较特殊，它的 name 即为 [document]
    print(soup.name)
    # 对于其他内部标签，输出的值便为标签本身的名称
    print(soup.title.name)

    # 获取tag对应的属性
    print(soup.a['href'])
    print(soup.a.get('href'))

    # NavigableString
    print(type(soup.a.string))


def commentObjTest():
    markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
    soup = BeautifulSoup(markup, 'html5lib')
    comment = soup.b.string
    print(type(comment))
    print(comment)


def stringsTest():
    from bs4 import element
    soup = BeautifulSoup(getHtmlStr(), 'html5lib')

    # 遍历head头
    head_tag = soup.head
    for c in head_tag:
        if isinstance(c, element.Tag):
            # stripped_strings 和 strings 都会返回一个字符串生成器
            # stripped_strings 除多余空白内容
            for s in c.stripped_strings:
                print(s)
            # print(c.stripped_strings)
            # print(c.strings)

    # soup.find_all()


def findTest():
    soup = BeautifulSoup(getHtmlStr(), 'html5lib')
    primaryDivTag = soup.find('div', attrs={'class': 'job-primary'})
    primaryDivTags = soup.find_all('div', attrs={'class': 'job-primary'})
    print(primaryDivTag)


def selectTest():
    soup = BeautifulSoup(getHtmlStr(), 'html5lib')

    # 填写css选择器 ,返回的是一个列表
    jobTitleDiv = soup.select('div .job-title')
    for dt in jobTitleDiv:
        print(dt.get_text())


if __name__ == '__main__':
    # tagElement()
    # commentObjTest()
    # stringsTest()
    # findTest()
    selectTest()

    pass
