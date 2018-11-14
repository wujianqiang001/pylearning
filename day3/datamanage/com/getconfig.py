#!/usr/bin/env python
# coding=utf-8
from configparser import ConfigParser
config = ConfigParser()
def getconf():
    config.read("config/config.ini")
    w = config.get("weather","w")
    t = config.get("time","t")
    c = config.get("cal","c")
    return w,t,c

if __name__ == "__main__":
    conf = getconf()
    print(conf)