#!/usr/bin/env python
# coding=utf-8
from com.getconfig import *
from com.readxlsx import *
from com.writexlsx import *

def getwtc():
    # w,t,c = getconf()
    # w = w.split(";")
    # t = t.split(";")
    # c = c.split(";")
    # return w,t,c
    k = lambda x:x.split(";")
    return map(k,getconf())

def getcontent():
    content = getxlsx()
    return content

def matchdata(content):
    w,t,c = getwtc()
    for w1 in w:
        if w1 in content:
            return "weather"
    for t1 in t:
        if t1 in content:
            return "time"
    for c1 in c:
        if c1 in content:
            return "cal"
    return "notmatch"

def main():
    content = getcontent()
    tagcontent = {}
    for cont in content:
        tag = matchdata(cont[5])
        # print("%s------------%s"%(cont[5],tag))
        # if not tagcontent.get(tag):
        #     tagcontent[tag] = [cont]
        # else:
        #     tagcontent[tag].append(cont)
        tagcontent.setdefault(tag,[]).append(cont)
    writedata(tagcontent)

if __name__ == "__main__":
    main()
    # t,w,c = getwtc()
    # print(t,w,c)