#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author  :  swolf.qu
# E-mail  :  swolf.qu@gmail.com
# Date    :  2018-04-28 10:22:57

import os
import re
import time
import webbrowser

import urllib.request
import urllib.parse

from bs4 import BeautifulSoup


def get_url_content(url, ua):
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-agent", ua)]
    return opener.open(url).read()


def get_news():
    # info = {}

    url = "http://edu.bjhd.gov.cn/gongkai/zxgk/"
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

    content = get_url_content(url, ua)

    soup = BeautifulSoup(markup=content, features="lxml")
    ul = soup.find("ul", class_="text_list")
    lis = ul.find_all("li")
    for li in lis:
        a = li.find("a")
        span = li.find("span")

        print("{} {} {}".format(a["title"], a["href"], span.text))

        url = urllib.parse.urljoin(
            "http://edu.bjhd.gov.cn/gongkai/zxgk/", a["href"])
        if re.search("2018年非本市户籍适龄儿童", a["title"]):
            webbrowser.open(url)


times = 0
if __name__ == "__main__":
    while True:
        os.system("clear")
        times += 1
        print("times: {} {}".format(times, time.ctime()))
        get_news()
        time.sleep(30)
