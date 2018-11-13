#!/usr/bin/env python
# coding=utf-8
import time,requests,platform
from PR2.day1.com.getmd5 import getmd5
if platform.python_version()[0] == "3":
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser
def surl(url):
    u1 = url.split("/")
    u3 = u1[-1].split(".")
    u4 = u3[0]
    if len(u4) > 10:
        u4 = u4[:10]
    u3[0] = u4
    u3 = ".".join(u3)
    u1[-1] = u3
    url = "/".join(u1)
    return url,u4
def skurl(url):
    u, u4 = surl(url)
    a = int(time.time()*100000)
    conf = ConfigParser()
    # conf.read("../config/config.ini")
    conf.read("config/config.ini")
    key = conf.get("keys","key")
    s = getmd5(u+str(a)+key)
    u1 = u + "?t=%d&k=%s"%(a,s)
    return u1

if __name__ == "__main__":

    url = "http://www.baidu.com/a/live/jkklkjjhkjkjkabc1rehj.ts"
    skurl(url)
    u, u4 = surl(url)
    key = "123456"
    for i in range(1):
        time.sleep(1)
        a = int(time.time()*100000)
        s = getmd5(u+str(a)+key)
        u1 = u + "?t=%d&k=%s"%(a,s)
        print(u1)
        r = requests.get(u1)
        print(r.status_code)
        print(r.content)