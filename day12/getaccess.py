#!/usr/bin/env python
# coding=utf-8
def getlog1():
    with open("access.log") as f:
        for i in f:
            yield i

g = getlog1()
for i in g:
    print(i)

