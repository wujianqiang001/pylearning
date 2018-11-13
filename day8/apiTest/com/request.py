#!/usr/bin/env python
# coding=utf-8
import requests
def get(url,headers=None):
    r = requests.get(url=url, headers=headers)
    return (r.status_code, r.text)