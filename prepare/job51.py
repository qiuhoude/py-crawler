#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import chardet
import random
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time


# 构造使用浏览器头部以及代理ip获取网页编码的函数
def getHtmlWithIp(url):
    # 浏览器头部
    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        # iPhone 6：
        "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

    ]
    # 代理ip
    proxies = [
        {'HTTPS': '116.77.206.56:80', 'HTTP': '116.1.11.19:80'},
        {'HTTPS': '106.75.226.36:808', 'HTTP': '106.75.225.83:808'},
        {'HTTPS': '175.18.215.50:80', 'HTTP': '61.135.217.7:80'},
        {'HTTPS': '175.148.159.199:80', 'HTTP': '118.190.95.35:9001'}
    ]
    # 异常处理
    try:
        # 获取响应内容
        response = requests.get(
            url,
            headers={'User_Agent': random.choice(user_agent)},
            proxies=random.choice(proxies)
        )
        # 获取编码
        code = chardet.detect(response.content)['encoding']
        # 解码
        response.encoding = code
        # 获取文本
        return response.text
    except Exception as e:
        print(e)
        time.sleep(1)
        global _times_count
        _times_count += 1
        if _times_count > 20:
            print('您的ip真的有问题')
            return
        print('第', _times_count, '次')
        getHtmlWithIp(url)


# 构造获取网页内容的函数
def getData(html, datalist):
    # 得到beautifulsoup对象
    soup = BeautifulSoup(html, 'html.parser')
    # 分析网页，提取内容
    # 遵循常用的规则：从大到小，先确定父元素，再确定子元素

    # 先获取指定内容的父元素
    parent = soup.find(id='resultList')
    # print(parent)
    # 通过父元素获取所有的子元素，可以避免父元素之外的class对el造成的影响
    # 获取所有 cless为el的div
    divs = parent.find_all('div', class_='el')
    # print(divs)
    # 使用for获取每个divs内的内容
    # 在实际操作过程中发现，第一次就报错，查看结构发现第一个没有P标签,删除它
    divs.pop(0)
    for each in divs:
        # 获取职位名
        jobName = each.find('p').get_text().strip()
        # 获取公司名
        company = each.find_all('span', recursive=False)[0].get_text()
        # 获取工作地点
        address = each.find_all('span', recursive=False)[1].text
        # 获取薪资
        sal = each.find_all('span', recursive=False)[2].text
        # 获取时间
        time = each.find_all('span', recursive=False)[3].text
        # print(time),
        datalist.append([jobName, company, address, sal, time])


# 构造存储到excel的函数
def saveToExcel(tablename, datalist):
    # 创建数据簿
    wb = Workbook()
    # 创建数据表
    ws = wb.active
    # 设置表格标题
    ws.title = tablename
    # 添加列标签
    ws.append(['职位名', '公司名', '工作地点', '薪资', '发布时间'])
    # for循环遍历
    for i in datalist:
        ws.append(i)
    # 保存工作簿命名为'表名.xlsx'
    wb.save(tablename + '.xlsx')


# 创建主函数
def main(jobName, n, tablename):
    for i in range(n):
        # 准备一个网址获取响应内容：
        url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,' + jobName + ',2,' + str(
            i + 1) + '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        # 获取网页内容
        html = getHtmlWithIp(url)
        # 创建一个列表，用来存放数据
        datalist = []
        # 执行函数获取数据
        getData(html, datalist)
        print('正在爬取第', i + 1, '页')
        time.sleep(1)
    # 执行函数将数据保存到excel
    saveToExcel(tablename, datalist)


if __name__ == '__main__':
    # 执行主函数：设置参数，即你想爬取的职位名称以及页数，工作簿的名称
    main('golang', 3, '人工智能职位表')
