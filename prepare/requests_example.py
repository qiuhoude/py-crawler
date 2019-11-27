#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
requests 使用
中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
github地址：https://github.com/requests/requests
"""

import requests

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}


def getTest():
    payload = {'wd': '湖北'}
    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get("http://www.baidu.com/s", params=payload, headers=headers)
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)
    # 查看响应内容，response.content返回的字节流数据
    # print(response.content)
    # print(response.raw.read(256))

    # 查看完整url地址
    print(response.url)

    # 查看响应头部字符编码
    print(response.encoding)

    # 查看响应码
    print(response.status_code)

    # 查看头信息
    print(response.headers)


def postTest():
    req = requests.request()


if __name__ == '__main__':
    getTest()
