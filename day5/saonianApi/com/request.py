#!/usr/bin/env python
# coding=utf-8
import requests,json
import re
from check import *
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
        return r
    if method == "post":
        pass