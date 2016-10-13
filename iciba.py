#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/03 18:54:36
"""
Get word info from iciba
"""
import sys
import urllib.request

from bs4 import BeautifulSoup
from bs4.element import NavigableString


def get_url_content(url, ua):
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-agent", ua)]
    return opener.open(url).read()


def get_word_info(word):
    info = {}

    url = "http://www.iciba.com/{}".format(word)
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

    content = get_url_content(url, ua)
    soup = BeautifulSoup(markup=content, features="lxml")

    # Get word
    wtags = soup.find_all("h1", class_="keyword")
    word = "".join(wtags[0].contents).strip()
    info["word"] = word

    # Get speaker
    speakers = []
    speaker_tags = soup.find("div", class_="base-speak")
    for tag in speaker_tags.children:
        if isinstance(tag, NavigableString):
            continue
        speakers.append(
            (tag.find("span").text, tag.find("i")["ms-on-mouseover"])
        )
    info["speakers"] = speakers

    # Get translate
    translate = []
    explain_tags = soup.find_all("ul", class_="base-list")
    lis = explain_tags[0].find_all("li")
    for li in lis:
        prop_tag = li.find("span", class_="prop")
        prop = prop_tag.text
        chinese_tag = li.find("p").find_all("span")
        chinese = " ".join([tag.text for tag in chinese_tag])
        translate.append([prop, chinese])
    info["translate"] = translate

    return info


def show_word_info(info):
    print(info["word"])
    print("-" * 30)
    for item in info["speakers"]:
        print(item[0])
    for item in info["translate"]:
        print("%s %s" % (item[0], item[1]))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: %s YourWord" % (sys.argv[0]))
        sys.exit(-1)
    for word in sys.argv[1:]:
        info = get_word_info(word)
        show_word_info(info)
