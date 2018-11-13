#!/usr/bin/env python
# coding=utf-8
a = [[1,2,3,4,5],[2,3,4,5,6]]
b = [[1,2,33,4,5],[2,3,5,5,6]]
#实现方式一：
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] != b[i][j]:
            print (a[i][j], b[i][j])

#实现方式二：
print [(a[i][j],b[i][j]) for i in range(len(a)) for j in range(len(a[0])) if a[i][j] != b[i][j]]

import datetime
a = datetime.datetime(2018, 1, 12)
b = datetime.datetime(2018, 4, 9)
print (b-a).days

c = [1,3,4,2,5,9,6]
for i in range(len(c)-1):
    for j in range(len(c)-1-i):
        if c[j] < c[j+1]:
            c[j],c[j+1] = c[j+1], c[j]
print c

import random
d = [1,2,3,4,5,6,7,8,9]
for i in range(len(d)):
    j = random.randint(0,i)
    d[i], d[j] = d[j], d[i]
print d

e = [1,2,3,3,4,5,3,2,1]
f = []
for i in e:
    if i not in f:
        f.append(i)
print f