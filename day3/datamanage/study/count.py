#!/usr/bin/env python
# coding=utf-8
data = ["a","b","c","a","b"]
d = {}
for a in data:
    # if not d.get(a):
    #     d[a] = 1#d[a] ：字典新增一个key
    # else:
    #     d[a] += 1 #d[a] ：获取字典key为a对应的值
    # print(d)
    d.setdefault(a,0)
    d[a] += 1
print(d)