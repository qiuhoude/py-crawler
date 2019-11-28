#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
requests 使用
中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
github地址：https://github.com/requests/requests
"""

import requests

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
headers = {
    "User-Agent": agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}


def getTest():
    payload = {'wd': '湖北'}
    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get("https://www.baidu.com/s", params=payload, headers=headers)
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    # print(response.text)

    # 查看响应内容，response.content返回的字节流数据
    # print(response.content.decode('utf-8'))
    # print(response.raw.read(256))
    with open("baidu.html", mode="w", encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))

    # 查看完整url地址
    print(response.url)

    # 查看响应头部字符编码
    print(response.encoding)

    # 查看响应码
    print(response.status_code)

    # 查看头信息
    print(response.headers)


def postTest():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    headers = {
        "User-Agent": agent,
        'Referer': 'https://www.lagou.com/jobs/list_golang?labelWords=&fromSearch=true&suginput=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        "Origin": "https://www.lagou.com",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "JSESSIONID=ABAAABAABEEAAJA940CFB0F4EA353D8A40BA30709EF6058; SEARCH_ID=d61fc436e8b14dffaf37c5a24149362a; user_trace_token=20191128112453-5a41406e-5b25-4dfc-9362-bcfc88408660; X_HTTP_TOKEN=42daf4b72327b2813941194751bf5e71415983ed09; WEBTJ-ID=20191128112453-16eb00a45871f0-05c494c884f5b7-b363e65-2073600-16eb00a458965b",
    }
    formData = {
        'first': True,
        'pn': 1,
        'kd': 'golang'
    }
    resp = requests.post(url, data=formData, headers=headers)
    # json 数据可以用json()方法来转成 dict
    # print(resp.content.decode('utf-8'))
    print(resp.json())


def proxyTest():
    proxies = {
        "http": "124.205.155.151:9090"
    }
    resp = requests.get("http://httpbin.org/ip", proxies=proxies)
    print(resp.json())


def cookieTest():
    url = "http://www.renren.com/PLogin.do"
    data = {"email": "970138074@qq.com", 'password': "pythonspider"}
    resp = requests.get('http://www.baidu.com/')
    print(resp.cookies)
    print(resp.cookies.get_dict())


def sessionTest():
    url = "http://www.renren.com/PLogin.do"
    data = {"email": "970138074@qq.com", 'password': "pythonspider"}
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    # requests.utils.add_dict_to_cookiejar()
    # 登录
    session = requests.session()
    session.post(url, data=data, headers=headers)

    # 访问大鹏个人中心
    resp = session.get('http://www.renren.com/880151247/profile')

if __name__ == '__main__':
    # getTest()
    # postTest()
    proxyTest()
    pass
