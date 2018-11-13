#!/usr/bin/env python
# coding=utf-8
import time
from PR1.day9.com.getmd5 import *
from configparser import ConfigParser
def surl(url):
    u1 = url.split("/")
    u2 = u1[-1]
    u3 = u2.split(".")
    u4 = u3[0]
    if len(u4)>32:
        u4 = u4[:32]
    u3[0] = u4
    u5 = ".".join(u3)
    u1[-1] = u5
    url = "/".join(u1)
    return url,u4

def skurl(url):
    url,u = surl(url)
    t = str(int(time.time()*1000))
    conf = ConfigParser()
    conf.read("config/config.ini")
    key = conf.get("keys","key")
    k = getmd5(u+t+key)
    url1 = url + "?t=%s&k=%s"%(t,k)
    return url1
if __name__ == "__main__":
    url = "http://www.baidu.com/a/b/live/home/abc123.ts"
    for i in range(10):
        time.sleep(0.1)
        url1 = skurl(url)
        print(url1)