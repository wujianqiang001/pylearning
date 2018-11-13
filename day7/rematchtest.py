#!/usr/bin/env python
# coding=utf-8
import re
a = "a|b|c|d"
# print(a.split("|"))
b = "jkkjkkj12345jkjkjkn456vjajfa;"
c = "jkjk;color=red,ll;l;"
d = "name=url; herf=<\"www.baidu.com\"> hight=90;"

# bb = re.search("n(\d+)v",b)
# print(bb.groups())
# bbb = re.findall("n(\d+)v",b)
# print(bbb)
# cc = re.search("color=(\w+)",c)
# print(cc.groups())
# ccc = re.search("color=(.+),",c)
# print(ccc.groups())
# dd = re.search("herf=<\"(.+)\">",d)
# print(dd.groups())
# phone = "kjjkfakjkf138-1234-4567jkjkjk,13812345678kjkjlk138-234-45678kjkjk"
# p = re.findall("(\d{3}-\d{4}-\d{4})",phone)
# print(p)
import os
def getdata():
    with open("access.log") as f:
        for line in f:
            yield line
f = open("useragent/sourcedata/accesslog.log","w")
i = 0
for line in getdata():
    f.write(line)
    i += 1
    if i >10000:
        break
f.close()
# os.system("python useragent/com/getuadata.py")
# os.system("python useragent/com/matchphones.py")
# os.system("python useragent/com/countphones.py")