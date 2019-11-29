#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from lxml import etree


def TestBossJob():
    # etree.HTML() # 解析字符串使用
    # htmlElement = etree.HTML("<a>哈哈<a/>")
    # print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
    html_parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse('boss_golang.html', parser=html_parser)
    jobDivs = html.xpath('//div[@class="job-primary"]')
    for index, jobDiv in enumerate(jobDivs):
        infoP = jobDiv.xpath('./div[1]')[0]
        jobTitle = infoP.xpath('.//div[@class="job-title"]/text()')[0]
        salary = infoP.xpath('.//span[@class="red"]/text()')[0]
        link = infoP.xpath('./h3/a/@href')[0]
        company = jobDiv.xpath('./div[2]//a/text()')[0]
        print(index, jobTitle, salary, company, "https://www.zhipin.com" + link)


if __name__ == '__main__':
    TestBossJob()
