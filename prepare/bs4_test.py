#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup


def getHtmlStr():
    with open("boss_golang.html", "r", encoding="utf-8") as fd:
        html = fd.read()
        return html


def parseStr():
    html = getHtmlStr()
    bs = BeautifulSoup(html, 'lxml')
    bs.find_all()


if __name__ == '__main__':
    parseStr()
