#!/usr/bin/env python
# coding=utf-8
import requests
def request(url):
    try:
        r = requests.get(url)
        return {"url":url,"code":r.status_code}
    except:
        return {"url":url,"code":502}