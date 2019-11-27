#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib import request
from urllib import parse


def urlopenTest():
    """
    url：请求的url。
    data：请求的data，如果设置了这个值，那么将变成post请求。
    返回值：返回值是一个http.client.HTTPResponse对象，这个对象是一个类文件句柄对象。有read(size)、readline、readlines以及getcode等方法。
    """
    resp = request.urlopen("http://www.baidu.com")
    print(resp.__dict__)
    print(resp._method)
    print(resp.status)
    print(resp.read().decode("utf-8"))
    # for l in resp.readlines():
    #     print(l.decode("utf-8"))


def urlretrieveTest():
    """
    这个函数可以方便的将网页上的一个文件保存到本地。以下代码可以非常方便的将百度的首页下载到本地：
    :return:
    """
    request.urlretrieve("https://static.runoob.com/images/demo/demo2.jpg", "a.jpg")


def parseTest():
    # 用浏览器发送请求的时候，如果url中包含了中文或者其他特殊字符，那么浏览器会自动的给我们进行编码。而如果使用代码发送请求，那么就必须手动的进行编码，
    # 这时候就应该使用urlencode函数来实现。urlencode可以把字典数据转换为URL编码的数据。示例代码如下：
    data = {'name': '爬虫', 'greet': 'hello world', 'age': 100}
    qs = parse.urlencode(data)
    print(qs)

    # 可以将经过编码后的url参数进行解码。示例代码如下：
    nd = parse.parse_qs(qs)
    print(nd)

    # 解析url
    url = "http://www.baidu.com/s;hello?wd=python&username=abc#1"
    ret = parse.urlparse(url)
    spRet = parse.urlsplit(url)  # 与urlparse 少了param
    print("ret:", ret)
    print("spRet:", spRet)
    print("netloc:", ret.netloc)
    print("scheme:", ret.scheme)


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}


def requestTest():
    url = "https://httpbin.org/get"
    req = request.Request(url, headers=headers, method="GET")
    req.add_header("Referer", "https://www.weibo.com/jobbole")
    resp = request.urlopen(req)
    print(resp.read().decode('utf-8'))


# 使用代理
def proxyTest():
    """
    设置代理
    西刺免费代理IP：http://www.xicidaili.com/
    快代理：http://www.kuaidaili.com/
    代理云：http://www.dailiyun.com/
    :return:
    """
    proxy_handler = request.ProxyHandler({"http": "136.228.128.14:61158"})
    nop_handler = request.ProxyHandler({})
    # 注意代理的 http 地址是https是不生效的
    url = "http://httpbin.org/get"
    opener = request.build_opener(proxy_handler)
    req = request.Request(url, headers=headers)
    resp = opener.open(req)
    print(resp.read().decode('utf-8'))


def cookieTest():
    """
    cookie的格式：
    Set-Cookie: NAME=VALUE；Expires/Max-age=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE
    NAME：cookie的名字。
    VALUE：cookie的值。
    Expires：cookie的过期时间。
    Path：cookie作用的路径。
    Domain：cookie作用的域名。
    SECURE：是否只在https协议下起作用。

    该模块主要的类有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。这四个类的作用分别如下：
    1. CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
    2. FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。
        filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。
    3. MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。
    4. LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。

    """

    from http.cookiejar import CookieJar
    # 创建cookie
    cookieJar = CookieJar()
    handler = request.HTTPCookieProcessor(cookieJar)
    opener = request.build_opener(handler)

    # 登陆
    data = {"email": "970138074@qq.com", "password": "pythonspider"}
    data = parse.urlencode(data).encode('utf-8')
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url, headers=headers, data=data)
    opener.open(req)

    # 访问
    url = 'http://www.renren.com/880151247/profile'
    req = request.Request(url, headers=headers)
    resp = opener.open(req)
    # 写文件
    with open('renren.html', 'w') as fp:
        fp.write(resp.read().decode("utf-8"))


def saveCookie():
    # 保存cookie到本地：
    from http.cookiejar import MozillaCookieJar

    cookiejar = MozillaCookieJar("cookie.txt")
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)

    req = request.Request("http://httpbin.org/cookies/set?name=qiu&age=28", headers=headers)
    resp = opener.open(req)
    print(resp.read().decode('utf-8'))
    cookiejar.save(ignore_expires=True, ignore_discard=True)


def loadCookie():
    from http.cookiejar import MozillaCookieJar

    cookiejar = MozillaCookieJar("cookie.txt")
    cookiejar.load(ignore_discard=True, ignore_expires=True)
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    req = request.Request("http://httpbin.org/cookies", headers=headers)
    resp = opener.open(req)
    print(resp.read().decode('utf-8'))


if __name__ == '__main__':
    # urlopenTest()
    # urlretrieveTest()
    # parseTest()
    # requestTest()
    # proxyTest()
    # cookieTest()
    saveCookie()
    loadCookie()
    pass
