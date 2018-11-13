#!/usr/bin/env python
# coding=utf-8
import requests,json
import re
from PR2.day4.saonianApi.check import *
def request(method,url,body,expection):
    if method == "get":
        r = requests.get(url,params=body)
        try:
            content = r.json()
            # print(content)
            check(content,expection)
        except:
            content=r.text
            url = re.findall("href=\"(.+?)\"",content)[0]
            r = requests.get(url)
            content = r.json()
            check(content,expection)
    if method == "post":
        pass